SET NAMES UTF8;
DROP DATABASE IF EXISTS qzss;
CREATE DATABASE qzss CHARSET=UTF8;
USE qzss;


create table user(
    id int unsigned not null auto_increment primary key,
    username varchar(20) not null,
    password varchar(32) not null,
    realname varchar(20) not null,
    img  varchar(100) not null default 'moren.gif',
    sex tinyint unsigned not null default '1'
);


create table admin(
    id int unsigned not null auto_increment primary key,
    username varchar(20) not null,
    password varchar(32) not null
);


create table advert(
    id int unsigned not null auto_increment primary key,
    img  varchar(100) not null,
    pos tinyint unsigned not null,
    url varchar(100) not null
);


create table class(
    id int unsigned not null auto_increment primary key,
    name varchar(50) not null
);


create table book(
    id int unsigned not null auto_increment primary key,
    name varchar(50) not null,
    writer varchar(50) not null,
    img  varchar(100) not null,
    info mediumtext not null,
    oldprice float(8,2) unsigned not null,
    nowprice float(8,2) unsigned not null,
    class_id int unsigned not null,
    stock int unsigned not null,
    sales int unsigned not null default '0',
    supplier int unsigned not null default '0',
    shelf tinyint unsigned not null,
    recommend tinyint unsigned not null default '0'
);


create table comment(
    id int unsigned not null auto_increment primary key,
    user_id int unsigned not null,
    content text,
    book_id int unsigned not null,
    time int
);


create table status(
    id int unsigned not null auto_increment primary key,
    name varchar(50)
);

create table indent(
    id int unsigned not null auto_increment primary key,
    code varchar(50) not null,
    user_id int unsigned not null,
    touch_id int unsigned not null,
    book_id int unsigned not null,
    price float(8,2) unsigned not null,
    num int unsigned not null,
    status_id int not null default '1',
    confirm tinyint unsigned not null default '0',
    paytype int unsigned not null default '1',
    posttype int unsigned not null default '1',
    time int not null
);


create table touch(
    id   int unsigned not null auto_increment primary key,
    name varchar(50) not null,
    addr varchar(100) not null,
    postcode varchar(10) not null,
    tel varchar(50) not null,
    user_id int unsigned not null
);


create table bookshelf(
    id   int unsigned not null auto_increment primary key,
    book_id int unsigned not null,
    user_id int unsigned not null
);