create database college DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
use college;
create table users(
  id int(5) not null primary key auto_increment,
  username char(64) not null,
  password char(32) not null default '',
  email char(128) not null,
  role tinyint(1) default 0
);
create table articles(
  id int(7) not null primary key auto_increment,
  title char(255),
  content text(65535),
  author int(5),
  type char(10)
);

insert into users(username,password,email,role) VALUES('admin1','admin1','admin1@mail.sysu.edu.cn','1');
insert into users(username,password,email,role) VALUES('user1','user1','user1@mail.sysu.edu.cn','0');
insert into article(title,content,author,type) VALUES('title1','content1','1','bgxx');
insert into article(title,content,author,type) VALUES('title2','content2','1','bgxx');
insert into article(title,content,author,type) VALUES('title3','content3','1','bgxx');
insert into article(title,content,author,type) VALUES('title4','content4','1','bkjxjw');
insert into article(title,content,author,type) VALUES('title5','content5','1','bkjxjw');
insert into article(title,content,author,type) VALUES('title6','content6','1','xsgz');
insert into article(title,content,author,type) VALUES('title7','content7','1','xsgz');
insert into article(title,content,author,type) VALUES('title8','content8','1','kyyyjs');
insert into article(title,content,author,type) VALUES('title9','content9','1','kyyyjs');
insert into article(title,content,author,type) VALUES('title10','content10','1','dwhzjl');
insert into article(title,content,author,type) VALUES('title11','content11','1','dwhzjl');
