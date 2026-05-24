-- ============================================================
--  Sistema de Biblioteca —  PostgreSQL
--  Desarrollo de Aplicaciones Web Lab 06
--  Autor: Basily
-- ============================================================

-- Activar extensión para UUIDs
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ============================================================
-- TABLA: users
-- Usuarios del sistema (administradores, bibliotecarios)
-- created_id y modified_id de todas las tablas referencian aquí
-- ============================================================
CREATE TABLE users (
    id           UUID         PRIMARY KEY DEFAULT uuid_generate_v4(),
    username     VARCHAR(50)  NOT NULL UNIQUE,
    email        VARCHAR(100) NOT NULL UNIQUE,
    password     VARCHAR(255) NOT NULL,
    role         VARCHAR(20)  NOT NULL DEFAULT 'librarian'
                              CHECK (role IN ('admin', 'librarian')),
    status       SMALLINT     NOT NULL DEFAULT 1,
    created      TIMESTAMP    NOT NULL DEFAULT NOW(),
    modified     TIMESTAMP    NOT NULL DEFAULT NOW(),
    created_id   UUID,
    modified_id  UUID
);

-- ============================================================
-- TABLA: categories
-- Genero de un libro
-- ============================================================
CREATE TABLE categories (
    id           UUID         PRIMARY KEY DEFAULT uuid_generate_v4(),
    name         VARCHAR(100) NOT NULL UNIQUE,
    description  TEXT,
    status       SMALLINT     NOT NULL DEFAULT 1,
    created      TIMESTAMP    NOT NULL DEFAULT NOW(),
    modified     TIMESTAMP    NOT NULL DEFAULT NOW(),
    created_id   UUID REFERENCES users(id),
    modified_id  UUID REFERENCES users(id)
);

-- ============================================================
-- TABLA: authors
-- Autores de libros
-- ============================================================
CREATE TABLE authors (
    id            UUID         PRIMARY KEY DEFAULT uuid_generate_v4(),
    names         VARCHAR(100) NOT NULL,
    fatherSurname VARCHAR(100),
    motherSurname VARCHAR(100),
    nationality   VARCHAR(50),
    status        SMALLINT     NOT NULL DEFAULT 1,
    created       TIMESTAMP    NOT NULL DEFAULT NOW(),
    modified      TIMESTAMP    NOT NULL DEFAULT NOW(),
    created_id    UUID REFERENCES users(id),
    modified_id   UUID REFERENCES users(id)
);

-- ============================================================
-- TABLA: books
-- Catalogo de libros disponibles en la biblioteca
-- Relación N:1 con categories
-- ============================================================
CREATE TABLE books (
    id              UUID         PRIMARY KEY DEFAULT uuid_generate_v4(),
    title           VARCHAR(255) NOT NULL,
    isbn            VARCHAR(20)  UNIQUE,
    stock           INTEGER      NOT NULL DEFAULT 1 CHECK (stock >= 0),
    editorial       VARCHAR(100),
    publicationYear SMALLINT,
    category_id     UUID REFERENCES categories(id),
    status          SMALLINT     NOT NULL DEFAULT 1,
    created         TIMESTAMP    NOT NULL DEFAULT NOW(),
    modified        TIMESTAMP    NOT NULL DEFAULT NOW(),
    created_id      UUID REFERENCES users(id),
    modified_id     UUID REFERENCES users(id)
);

-- ============================================================
-- TABLA: members
-- Socios/lectores registrados en la biblioteca
-- Relacion 1:1 con users (si el socio tiene acceso al sistema)
-- ============================================================
CREATE TABLE members (
    id             UUID         PRIMARY KEY DEFAULT uuid_generate_v4(),
    names          VARCHAR(100) NOT NULL,
    fatherSurname  VARCHAR(100) NOT NULL,
    motherSurname  VARCHAR(100),
    email          VARCHAR(100) UNIQUE,
    phone          VARCHAR(20),
    address        TEXT,
    membershipDate DATE         NOT NULL DEFAULT CURRENT_DATE,
    user_id        UUID         REFERENCES users(id),
    status         SMALLINT     NOT NULL DEFAULT 1,
    created        TIMESTAMP    NOT NULL DEFAULT NOW(),
    modified       TIMESTAMP    NOT NULL DEFAULT NOW(),
    created_id     UUID REFERENCES users(id),
    modified_id    UUID REFERENCES users(id)
);

-- ============================================================
-- TABLA: authors_books  (N:M — ordenada alfabéticamente)
-- Relación entre autores y libros
-- ============================================================
CREATE TABLE authors_books (
    id           UUID      PRIMARY KEY DEFAULT uuid_generate_v4(),
    author_id    UUID      NOT NULL REFERENCES authors(id),
    book_id      UUID      NOT NULL REFERENCES books(id),
    status       SMALLINT  NOT NULL DEFAULT 1,
    created      TIMESTAMP NOT NULL DEFAULT NOW(),
    modified     TIMESTAMP NOT NULL DEFAULT NOW(),
    created_id   UUID REFERENCES users(id),
    modified_id  UUID REFERENCES users(id),
    UNIQUE (author_id, book_id)
);

-- ============================================================
-- TABLA: loans
-- Registro de préstamos de libros a socios
-- Relación N:1 con members y N:1 con books
-- ============================================================
CREATE TABLE loans (
    id           UUID      PRIMARY KEY DEFAULT uuid_generate_v4(),
    member_id    UUID      NOT NULL REFERENCES members(id),
    book_id      UUID      NOT NULL REFERENCES books(id),
    loanDate     DATE      NOT NULL DEFAULT CURRENT_DATE,
    dueDate      DATE      NOT NULL,
    returnDate   DATE,
    status       SMALLINT  NOT NULL DEFAULT 1,
    created      TIMESTAMP NOT NULL DEFAULT NOW(),
    modified     TIMESTAMP NOT NULL DEFAULT NOW(),
    created_id   UUID REFERENCES users(id),
    modified_id  UUID REFERENCES users(id)
);

-- ============================================================
-- INDICES para mejorar rendimiento en consultas frecuentes
-- ============================================================
CREATE INDEX idx_books_category    ON books(category_id);
CREATE INDEX idx_authors_books_book   ON authors_books(book_id);
CREATE INDEX idx_authors_books_author ON authors_books(author_id);
CREATE INDEX idx_loans_member      ON loans(member_id);
CREATE INDEX idx_loans_book        ON loans(book_id);
CREATE INDEX idx_members_user      ON members(user_id);