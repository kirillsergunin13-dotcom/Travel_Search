CREATE TABLE IF NOT EXISTS treavels
(
    -- Уникальный идентификатор записи генерируется базой данных.
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    telegram_id bigint NOT NULL,
    city character varying(100) NOT NULL,
    date date NOT NULL,
    hotel_text character varying(5000) NOT NULL,
    cafe_text character varying(5000) NOT NULL
)