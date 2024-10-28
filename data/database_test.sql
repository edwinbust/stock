#TABLA USERS
INSERT INTO users (id, username, email, password, role, status, photo) VALUES ('1', 'System Admin', 'sysadmin@criptoeducando.edu', 'bd4855ccb5a2e8619f469b9b0061896c1a9803ae18b17df43', 'admin', '1', 'NGzYWI5NjAzOWY2ZTczZDQyM2M5ZmYzNjMwMNZY2JiYjdhYmVmMTAxNFiCgoKCg==');
INSERT INTO users (id, username, email, password, role, status, photo) VALUES ('2', 'Antonio A', 'antonio.a@example.com', '6303bbb7abef10151bfc958d2a627b39c88289a4ab', 'user', '1', 'NjMwM2JiYjdhYmVmMTAxNTFiZmM5NThkMmE2MjdiMzljODgyODlhNGFiCg==');
INSERT INTO users (id, username, email, password, role, status, photo) VALUES ('3', 'Edi B', 'edi.b@example.com', 'beee0c4664c60e8a48ad4d3ab96039f6e73d40c3a2', 'user', '1', 'YmVlZTBjNDY2NGM2MGU4YTQ4YWQ0ZDNhYjk2MDM5ZjZlNzNkNDBjM2EyCg==');
INSERT INTO users (id, username, email, password, role, status, photo) VALUES ('4', 'Erip M', 'erip.m@example.com', '851c0f09b96550ca0203197856948c423c9ba65a9a', 'user', '1', 'ODUxYzBmMDliOTY1NTBjYTAyMDMxOTc4NTY5NDhjNDIzYzliYTY1YTlhCgo=');
INSERT INTO users (id, username, email, password, role, status, photo) VALUES ('5', 'Ana I', 'ana.i@example.com', '800c4664c60e8a48ad4d3ab96039f6e73d423c9ff3', 'user', '1', 'ODAwYzQ2NjRjNjBlOGE0OGFkNGQzYWI5NjAzOWY2ZTczZDQyM2M5ZmYzCgoK');
INSERT INTO users (id, username, email, password, role, status, photo) VALUES ('6', 'Caty A', 'caty.a@example.com', '4d3ab96039f6e73d423c9ff36303bbb7abef10151b', 'user', '1', 'NGQzYWI5NjAzOWY2ZTczZDQyM2M5ZmYzNjMwM2JiYjdhYmVmMTAxNTFiCgoKCg==');

#TABLA fund_operations
INSERT INTO fund_operations (id, funde_inv, profit_funde, funde_porc_share, funde_now, timestamp, transactions) VALUES ('1', '1500', '0', '0', '1500', 'Fri Oct 25 10:46:07 -03 2024', '1');

#TABLA fund_transactions
INSERT INTO fund_transactions (id, user_id, inv_user, operation_id, profit_user, porc_share, share_now, is_latest) VALUES ('1', '1', '0', '1', '0', '0', '0', '1');
INSERT INTO fund_transactions (id, user_id, inv_user, operation_id, profit_user, porc_share, share_now, is_latest) VALUES ('2', '2', '500', '1', '0', '33.33', '500', '1');
INSERT INTO fund_transactions (id, user_id, inv_user, operation_id, profit_user, porc_share, share_now, is_latest) VALUES ('3', '3', '100', '1', '0', '6.67', '100', '1');
INSERT INTO fund_transactions (id, user_id, inv_user, operation_id, profit_user, porc_share, share_now, is_latest) VALUES ('4', '4', '350', '1', '0', '23.33', '350', '1');
INSERT INTO fund_transactions (id, user_id, inv_user, operation_id, profit_user, porc_share, share_now, is_latest) VALUES ('5', '5', '400', '1', '0', '26.67', '400', '1');
INSERT INTO fund_transactions (id, user_id, inv_user, operation_id, profit_user, porc_share, share_now, is_latest) VALUES ('6', '6', '150', '1', '0', '10.00', '150', '1');
