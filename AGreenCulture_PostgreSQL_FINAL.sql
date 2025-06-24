-- Active: 1747882712720@@127.0.0.1@5432@agreenculture
-- Active: 1747882712720@@127.0.0.1@5432@postgres
-- Conectar a la base de datos (ejecutar fuera de la sesión psql)
-- CREATE DATABASE agreenculture;
-- \c agreenculture;




-- Tabla de roles de usuario
drop table if exists user_roles cascade;
create table user_roles (
    id serial primary key,
    role_name varchar(50),
    created_at timestamp default current_timestamp
);

-- Tabla de usuarios (AUTH_USER)
drop table if exists users cascade;
create table users (
    id serial primary key,
    username varchar(100) unique not null,
    email varchar(100) unique not null,
    password text not null,
    first_name varchar(100),
    last_name varchar(100),
    is_active boolean default true,
    is_superuser boolean default false,
    is_staff boolean default false,
    last_login timestamp null,
    date_joined timestamp default current_timestamp,
    user_role_id integer,
    foreign key (user_role_id) references user_roles(id)
);

-- Tabla de direcciones
drop table if exists address_book cascade;
create table address_book (
    id serial primary key,
    user_id integer not null,
    address text,
    label varchar(50),
    is_default boolean default false,
    foreign key (user_id) references users(id)
);

-- Tabla de tipos de granja
drop table if exists type_farm cascade;
create table type_farm (
    id serial primary key,
    name varchar(100),
    description text
);

-- Tabla de granjas
drop table if exists farms cascade;
create table farms (
    id serial primary key,
    user_id integer not null,
    name varchar(100) not null,
    description text,
    location varchar(200),
    type_id integer,
    created_at timestamp default current_timestamp,
    foreign key (user_id) references users(id),
    foreign key (type_id) references type_farm(id)
);

-- Tabla de categorías
drop table if exists categories cascade;
create table categories (
    id serial primary key,
    name varchar(100) unique not null,
    description text
);

-- Tabla de productos (sin category_id)
drop table if exists products cascade;
create table products (
    id serial primary key,
    farm_id integer not null,
    name varchar(100) not null,
    description text,
    price numeric(10,2) not null,
    quantity integer not null,
    image_url text,
    created_at timestamp default current_timestamp,
    foreign key (farm_id) references farms(id)
);

-- Relación muchos a muchos entre productos y categorías
drop table if exists product_category cascade;
create table product_category (
    product_id integer not null,
    category_id integer not null,
    primary key (product_id, category_id),
    foreign key (product_id) references products(id),
    foreign key (category_id) references categories(id)
);

-- Tabla de lotes de producción de una granja
drop table if exists farm_batches cascade;
create table farm_batches (
    id serial primary key,
    farm_id integer not null,
    quantity integer not null,
    production_date date not null,
    measurement_type varchar(50),
    created_at timestamp default current_timestamp,
    foreign key (farm_id) references farms(id)
);

-- Tabla de disponibilidad de productos
drop table if exists product_availability cascade;
create table product_availability (
    id serial primary key,
    product_id integer not null,
    status varchar(50),
    created_at timestamp default current_timestamp,
    foreign key (product_id) references products(id)
);

-- Tabla de estadísticas de productos
drop table if exists product_statistic cascade;
create table product_statistic (
    id serial primary key,
    product_id integer not null,
    times_sold integer default 0,
    times_favorited integer default 0,
    foreign key (product_id) references products(id)
);

-- Tabla de estados de pedido
drop table if exists status_order cascade;
create table status_order (
    id serial primary key,
    status varchar(50)
);

-- Tabla de pedidos
drop table if exists orders cascade;
create table orders (
    id serial primary key,
    buyer_id integer not null,
    total_amount numeric(10,2),
    payment_method varchar(50),
    status_id integer,
    delivery_address text,
    created_at timestamp default current_timestamp,
    foreign key (buyer_id) references users(id),
    foreign key (status_id) references status_order(id)
);

-- Detalles de pedidos
drop table if exists order_items cascade;
create table order_items (
    id serial primary key,
    order_id integer not null,
    product_id integer not null,
    quantity integer not null,
    unit_price numeric(10,2) not null,
    foreign key (order_id) references orders(id),
    foreign key (product_id) references products(id)
);

-- Reseñas
drop table if exists reviews cascade;
create table reviews (
    id serial primary key,
    buyer_id integer not null,
    farm_id integer not null,
    rating integer,
    comment text,
    created_at timestamp default current_timestamp,
    foreign key (buyer_id) references users(id),
    foreign key (farm_id) references farms(id)
);

-- Tips de clima
drop table if exists weather_tips cascade;
create table weather_tips (
    id serial primary key,
    farm_id integer not null,
    location varchar(100),
    weather_data json,
    tip text,
    created_at timestamp default current_timestamp,
    foreign key (farm_id) references farms(id)
);

-- Mensajes
drop table if exists messages cascade;
create table messages (
    id serial primary key,
    sender_id integer not null,
    receiver_id integer not null,
    message text not null,
    sent_at timestamp default current_timestamp,
    foreign key (sender_id) references users(id),
    foreign key (receiver_id) references users(id)
);

-- Favoritos
drop table if exists favorites cascade;
create table favorites (
    id serial primary key,
    buyer_id integer not null,
    product_id integer not null,
    note text,
    favorited_at timestamp default current_timestamp,
    foreign key (buyer_id) references users(id),
    foreign key (product_id) references products(id)
);

-- Reportes
drop table if exists reports cascade;
create table reports (
    id serial primary key,
    user_id integer not null,
    product_id integer not null,
    title varchar(100),
    reason text,
    created_at timestamp default current_timestamp,
    foreign key (user_id) references users(id),
    foreign key (product_id) references products(id)
);
