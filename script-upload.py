from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from models import User, FundOperation, FundTransaction  # Asegúrate de importar tus modelos definidos
from datetime import datetime

# Configuración de la conexión a la base de datos
DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

def create_fund_operation(profit_funde):
    try:
        # Obtener usuarios activos
        active_users = session.query(User).filter(User.status == 'True').all()

        # Calcular funde_inv sumando inv_user de usuarios activos
        funde_inv = sum(user_transaction.inv_user for user in active_users for user_transaction in user.investments)

        # Calcular funde_porc_share
        funde_porc_share = (profit_funde / funde_inv) * 100 if funde_inv != 0 else 0

        # Calcular funde_now
        funde_now = funde_inv + profit_funde

        # Crear operación del fondo
        new_operation = FundOperation(
            funde_inv=funde_inv,
            profit_funde=profit_funde,
            funde_porc_share=funde_porc_share,
            funde_now=funde_now,
            timestamp=datetime.now()
        )
        session.add(new_operation)
        session.commit()
        
        # Distribuir ganancia/pérdida entre los usuarios activos
        for user in active_users:
            # Obtener última transacción del usuario y actualizar a no vigente
            last_transaction = session.query(FundTransaction).filter(
                and_(FundTransaction.user_id == user.id, FundTransaction.is_latest == True)
            ).first()
            if last_transaction:
                last_transaction.is_latest = False
            
            # Obtener inv_user y calcular porc_share
            inv_user = last_transaction.inv_user
            porc_share = (inv_user / funde_inv) * 100 if funde_inv != 0 else 0

            # Calcular profit_user y share_now
            profit_user = (porc_share * profit_funde) / 100
            share_now = inv_user + profit_user

            # Crear nueva transacción para el usuario
            new_transaction = FundTransaction(
                user_id=user.id,
                operation_id=new_operation.id,
                inv_user=inv_user,
                profit_user=profit_user,
                porc_share=porc_share,
                share_now=share_now,
                is_latest=True
            )
            session.add(new_transaction)
        
        # Confirmar transacciones
        session.commit()
        print("Operación y transacciones de usuarios actualizadas exitosamente.")
    
    except Exception as e:
        session.rollback()
        print(f"Error al crear la operación del fondo: {e}")
    finally:
        session.close()

# Ejemplo de uso: crear operación del fondo con una ganancia/pérdida dada
profit_funde_input = 500  # El valor de profit_funde debe ingresarse
create_fund_operation(profit_funde_input)
