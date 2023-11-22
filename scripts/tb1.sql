CREATE TABLE transaction (
    id SERIAL PRIMARY KEY,
    account_id VARCHAR(36) NOT NULL,
    destination_account_id VARCHAR(36) NOT NULL,
    amount DECIMAL(9,9) NOT NULL,
    transaction_type VARCHAR(10) NOT NULL,
    transaction_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);