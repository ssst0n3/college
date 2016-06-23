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
insert into articles(title,content,author,type) VALUES('资讯管理学院“两学一做”专题党课学习顺利举行','2016年5月30日，响应学校“两学一做”学习教育活动号召，根据学院实施方案的安排，各教职工党支部、研究生党支部及本科生党支部联合举行“两学一做”专题学习活动，学院党委王琤书记应邀为全体师生党员上党课。会上，王琤书记以《从“上善若水”说开去》为题，分享自己的学习体会。王书记首先引用了《道德经》里的典故上善若水”，从水的美德入手，介绍了水刚柔并济、随物赋形等特点所承载的美德。介绍了习平总书记讲话中引用的一系列关于水的典故：鼓励人民群众发扬‘滴水穿石’般的韧劲和默默奉献的艰苦创业精神；发挥“海纳百川，有容乃大”的精神进行国际合作等。结合自身实际，希望在的各位党员可以学习“水”的美德，以刚柔并济的标准来要求自身，艰苦奋斗、无私坦荡，争取做一名如水一般纯净无暇的合格共产党员。王书记又从水的美德谈到了中山大学的办学理念。书记提出，教师、学生、职员，共同组成了大学这个学术共同体，也是托起大学这艘船并使其驶向学术彼岸的“水”。由此引申出“确立教授在学校务中的学术主导地位”和“将培育学生放在学校工作的核心位置”的理念。同时期望在座的各位教职工学习中山大学的名家大师们“以水为德”的品质，发挥滴水穿石的精神，不断追求更高的学术科研水平。最后，书记以罗俊校长提出的人才培养目标作为结束语，鼓励在座的所有学生党员能够学德才兼备，怀领袖气质，树家国情怀，以“上善若水”之境。最后，陈定权副院长、张洋教授、黄涛副书记和张靖常务副院长等教师党员先后围绕王铮书记的讲话与大在座党员畅谈想法与收获。各教工党支部、研究生党支部以及各本科生党支部也分别派代表就本次的党会主题进行了发言。大家纷纷表示从王书记的讲话中收获颇多，并将在未来的学习与生活中用心体悟水的美德，不断地严格要求自己，做一名优秀的共产党员。','1','bgxx');
insert into articles(title,content,author,type) VALUES('title2','content2','1','bgxx');
insert into articles(title,content,author,type) VALUES('title3','content3','1','bgxx');
insert into articles(title,content,author,type) VALUES('title4','content4','1','bkjxjw');
insert into articles(title,content,author,type) VALUES('title5','content5','1','bkjxjw');
insert into articles(title,content,author,type) VALUES('title6','content6','1','xsgz');
insert into articles(title,content,author,type) VALUES('title7','content7','1','xsgz');
insert into articles(title,content,author,type) VALUES('title8','content8','1','kyyyjs');
insert into articles(title,content,author,type) VALUES('title9','content9','1','kyyyjs');
insert into articles(title,content,author,type) VALUES('title10','content10','1','dwhzjl');
insert into articles(title,content,author,type) VALUES('title11','content11','1','dwhzjl');
