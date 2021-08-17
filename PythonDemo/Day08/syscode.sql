create table syscode(
  fid integer primary key autoincrement not null,
  fname text(20) not null,
	fcode  text(20) not null,
	fvalue  text(20) not null,
	isv    text(1) not null
);