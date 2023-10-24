CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    telegram_id INT,
    is_admin BOOLEAN DEFAULT FALSE,
    date_created TIMESTAMP WITH TIME ZONE,
    date_updated TIMESTAMP WITH TIME ZONE DEFAULT NULl,
    data_deleted TIMESTAMP WITH TIME ZONE DEFAULT NULl

);

CREATE TABLE IF NOT EXISTS tags (
    id SERIAL PRIMARY KEY,
    user_id INT,
    name TEXT NOT NULL,
    date_created TIMESTAMP WITH TIME ZONE,
    date_updated TIMESTAMP WITH TIME ZONE DEFAULT NULl,
    data_deleted TIMESTAMP WITH TIME ZONE DEFAULT NULl,

    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS message_hub (
    id SERIAL PRIMARY KEY,
    user_id INT,
    tag_id INT,
    descrition TEXT,
    mes_tg_id TEXT,
    mes_name TEXT,
    mes_type TEXT,
    date_created TIMESTAMP WITH TIME ZONE,
    date_updated TIMESTAMP WITH TIME ZONE DEFAULT NULl,
    data_deleted TIMESTAMP WITH TIME ZONE DEFAULT NULl,

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (tag_id) REFERENCES tags(id)
);