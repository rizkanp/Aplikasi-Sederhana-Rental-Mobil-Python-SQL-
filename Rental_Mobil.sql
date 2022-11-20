#create database rental;

show databases;

use rental;

create table mobil(
	Nama_mobil varchar(255),
    Warna_mobil varchar(255),
    Harga_mobil int,
    Sopir varchar(255),
    Plat_Nomor int
);

show tables;
select * from mobil;
insert into mobil values ('Pajero', 'Hitam', 500000, 'Dengan Sopir', 001);
insert into mobil values ('Pajero', 'Putih', 500000, 'Dengan Sopir', 002);
insert into mobil values ('Pajero', 'Hitam', 400000, 'Tanpa Sopir', 003);
insert into mobil values ('Pajero', 'Putih', 400000, 'Tanpa Sopir', 004);

SELECT * from mobil;

