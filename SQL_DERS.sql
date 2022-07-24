-- DDL (Data Definition Language)

-- create -> oluşturma
-- alter -> güncelleme
-- drop -> silme


-- TABLO OLUŞTURMA
CREATE TABLE accounts
(
    id         SERIAL PRIMARY KEY,
    user_name  VARCHAR(50) UNIQUE  NOT NULL,
    password   VARCHAR(100)        NOT NULL,
    email      VARCHAR(100) UNIQUE NOT NULL,
    created_on TIMESTAMP           NOT NULL
);

--TABLOYA VERİ EKLEME
INSERT INTO accounts(user_name, password, email, created_on)
VALUES ('mehmetnuri', '123456', 'info@mehmetnuri.net', current_timestamp);

INSERT INTO accounts(user_name, password, email, created_on)
VALUES ('aycacakmakoglu', 'ayca34', 'aycacakmak@capa.edu.tr', current_timestamp);

INSERT INTO accounts(user_name, password, email, created_on)
VALUES ('yusuf_yusa', 'kajsdlkasjd', 'yusuf@yusa.com', current_timestamp);

-- VERİ ÇEKME
SELECT * FROM accounts; -- BUTÜN KOLONLARIYLA BİRLİKTE accounts TABLOSUNDAKİ VERİLERİ GETİR

SELECT user_name, email FROM accounts; -- BELİRLİ KOLONLARI GETİR

SELECT * FROM accounts WHERE id = 4;
SELECT * FROM accounts WHERE user_name =  'mehmetnuri'; -- TAM EŞLEME
SELECT * FROM accounts WHERE user_name LIKE 'm%'; -- M İLE BAŞLAYAN
SELECT * FROM accounts WHERE user_name LIKE '%ri'; --Rİ İLE BİTEN KAYITLAR
SELECT * FROM accounts WHERE user_name LIKE '%mehmetnuri%'; -- İÇERİSİNDE mehmetnuri OLAN KAYITLAR

SELECT * FROM accounts WHERE id > 1;
SELECT * FROM accounts WHERE id IN (3,6,8);
SELECT * FROM accounts WHERE id BETWEEN 3 AND 8;
SELECT * FROM accounts WHERE id <> 1; --EŞİT DEĞİL
SELECT * FROM accounts WHERE id != 1; -- EŞİT DEĞİL
SELECT * FROM accounts WHERE id IS NOT  NULL;
SELECT * FROM accounts WHERE id >= 2;
SELECT * FROM accounts WHERE id <= 8;
SELECT * FROM accounts WHERE id = 3 OR id = 8;

SELECT  * FROM accounts WHERE length(user_name) BETWEEN 1 AND 11 ORDER BY user_name; -- a-z ye sıralar
SELECT  * FROM accounts WHERE length(user_name) BETWEEN 1 AND 11 ORDER BY user_name desc ;-- z-a ya sıralar

-- TABLOYA YENİ KOLON EKLEME
ALTER  TABLE accounts ADD COLUMN birth_year INT;

-- VERİ GÜNCELLEME
UPDATE accounts SET birth_year = 1993 WHERE id = 1;
UPDATE accounts SET birth_year = 1900 WHERE birth_year IS NULL;

-- TABLO ADI GÜNCELLEME
ALTER TABLE accounts RENAME TO hesaplar;



CREATE  TABLE  contacts(
    id SERIAL PRIMARY KEY ,
    account_id INT,
    contact_name VARCHAR(100) NOT NULL ,
    phone VARCHAR(15) NOT NULL ,
    email varchar(100),

    CONSTRAINT  FK_ACCOUNTS
                       FOREIGN KEY (account_id)
                       REFERENCES accounts(id)
);

INSERT INTO contacts(account_id, contact_name, phone, email)
VALUES (1, 'Ahmet', '5663322211', 'ahmet@xx.com');

-- YANLIŞ KULLANIM
SELECT * FROM contacts
LEFT JOIN accounts a on a.id = contacts.account_id WHERE a.id = 1;

-- DOĞRU KULLANIM
SELECT contacts.contact_name, contacts.phone, contacts.email FROM contacts
LEFT JOIN accounts a on a.id = contacts.account_id WHERE a.id = 1;

SELECT * FROM contacts
INNER JOIN accounts a ON a.id = contacts.account_id;

SELECT * FROM contacts
RIGHT JOIN  accounts a ON a.id = contacts.account_id;


CREATE TABLE employee
(
    id  SERIAL PRIMARY KEY ,
    first_name VARCHAR(100) NOT NULL ,
    last_name VARCHAR(100) NOT NULL ,
    manager_id INT,

    FOREIGN KEY (manager_id)
    REFERENCES employee(id)
    ON DELETE CASCADE
    ON UPDATE  CASCADE

);


INSERT INTO employee(first_name, last_name, manager_id)
VALUES
    ('AHMET', 'KOÇ', NULL),
    ('HASAN', 'KALYONCU', 1),
    ('MURAT', 'DOĞRAMACI', 1),
    ('KEMAL', 'DERVİŞ', 2),
    ('MUSTAFA', 'BURAK', 2),
    ('CENGİZ', 'KURT', 3),
    ('CEZMİ', 'KALORİFER', 3);


SELECT concat(m.first_name, ' ', m.last_name) as name_surname FROM employee e
INNER JOIN employee m ON m.manager_id = e.id where e.id=2;

DROP TABLE  IF EXISTS employee;

DELETE FROM contacts WHERE id =3;
