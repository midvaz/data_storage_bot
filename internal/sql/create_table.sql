CREATE TABLE IF NOT EXISTS users (
    id SERIAL ,
    telegram_id INT PRIMARY KEY,
    is_admin BOOLEAN DEFAULT FALSE,
    date_created TIMESTAMP WITH TIME ZONE,
    date_updated TIMESTAMP WITH TIME ZONE DEFAULT NULl,
    data_deleted TIMESTAMP WITH TIME ZONE DEFAULT NULl

);

CREATE TABLE IF NOT EXISTS tags (
    id SERIAL PRIMARY KEY,
    user_tg_id INT,
    name TEXT NOT NULL,
    date_created TIMESTAMP WITH TIME ZONE,
    date_updated TIMESTAMP WITH TIME ZONE DEFAULT NULl,
    data_deleted TIMESTAMP WITH TIME ZONE DEFAULT NULl,

    FOREIGN KEY (user_tg_id) REFERENCES users(telegram_id)
);

CREATE TABLE IF NOT EXISTS message_hub (
    id SERIAL PRIMARY KEY,
    user_tg_id INT,
    tag_id INT,
    descrition TEXT,
    mes_tg_id TEXT,
    mes_name TEXT,
    mes_type TEXT,
    date_created TIMESTAMP WITH TIME ZONE,
    date_updated TIMESTAMP WITH TIME ZONE DEFAULT NULl,
    data_deleted TIMESTAMP WITH TIME ZONE DEFAULT NULl,

    FOREIGN KEY (user_tg_id) REFERENCES users(telegram_id),
    FOREIGN KEY (tag_id) REFERENCES tags(id)
);