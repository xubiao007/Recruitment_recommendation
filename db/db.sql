-- we don't know how to generate root <with-no-name> (class Root) :(
create table User_information_user
(
	id integer not null
		primary key autoincrement,
	name varchar(20) not null
		unique,
	email varchar(30) not null,
	phone varchar(11) not null,
	edu varchar(10) not null,
	major varchar(20) not null,
	title varchar(20),
	skill varchar(20),
	exp varchar(20),
	sex varchar(10) not null,
	address varchar(60),
	image varchar(100) not null,
	pwd varchar(128) not null
);

create table Reptile_task_text
(
	id integer not null
		primary key autoincrement,
	job_key varchar(30) not null,
	total_page integer,
	state varchar(16),
	date datetime not null,
	user_text_id bigint not null
		references User_information_user
			deferrable initially deferred,
	required_page integer,
	run_time varchar(20)
);

create table Job_information_work
(
	id integer not null
		primary key autoincrement,
	job varchar(50) not null,
	salary varchar(20) not null,
	city varchar(20) not null,
	exp varchar(20),
	edu varchar(10),
	job_num varchar(20),
	company varchar(60) not null,
	welfare varchar(100),
	job_url varchar(120) not null,
	company_url varchar(120) not null,
	rep_work_id bigint not null
		references Reptile_task_text
			deferrable initially deferred
);

create table Collection_management_collection
(
	id integer not null
		primary key autoincrement,
	job_id_id bigint not null
		unique
		references Job_information_work
			deferrable initially deferred,
	user_id_id bigint not null
		references User_information_user
			deferrable initially deferred
);

create index Collection_management_collection_user_id_id_d26d4b9c
	on Collection_management_collection (user_id_id);

create table Detail_job_info_detail
(
	id integer not null
		primary key autoincrement,
	attribute varchar(80) not null,
	english varchar(20),
	job_info text not null,
	address varchar(30) not null,
	"release" varchar(20) not null,
	cp_nature varchar(20) not null,
	cp_scale varchar(60),
	cp_industry varchar(20),
	cp_info text not null,
	job_detail_id bigint not null
		unique
		references Job_information_work
			deferrable initially deferred
);

create index Job_information_work_rep_work_id_9fe2a197
	on Job_information_work (rep_work_id);

create table Recommended_information_recommend
(
	id integer not null
		primary key autoincrement,
	rate real,
	job_rec_id bigint not null
		unique
		references Job_information_work
			deferrable initially deferred,
	user_rec_id bigint not null
		references User_information_user
			deferrable initially deferred
);

create index Recommended_information_recommend_user_rec_id_daf19b85
	on Recommended_information_recommend (user_rec_id);

create index Reptile_task_text_user_text_id_3c01fe43
	on Reptile_task_text (user_text_id);

create table User_information_await
(
	id integer not null
		primary key autoincrement,
	type varchar(10) not null,
	city varchar(10) not null,
	major varchar(16),
	position varchar(20),
	user_await_id bigint not null
		references User_information_user
			deferrable initially deferred,
	date datetime not null
);

create index User_information_await_user_await_id_c652dae6
	on User_information_await (user_await_id);

create table auth_group
(
	id integer not null
		primary key autoincrement,
	name varchar(150) not null
		unique
);

create table auth_user
(
	id integer not null
		primary key autoincrement,
	password varchar(128) not null,
	last_login datetime,
	is_superuser bool not null,
	username varchar(150) not null
		unique,
	last_name varchar(150) not null,
	email varchar(254) not null,
	is_staff bool not null,
	is_active bool not null,
	date_joined datetime not null,
	first_name varchar(150) not null
);

create table auth_user_groups
(
	id integer not null
		primary key autoincrement,
	user_id integer not null
		references auth_user
			deferrable initially deferred,
	group_id integer not null
		references auth_group
			deferrable initially deferred
);

create index auth_user_groups_group_id_97559544
	on auth_user_groups (group_id);

create index auth_user_groups_user_id_6a12ed8b
	on auth_user_groups (user_id);

create unique index auth_user_groups_user_id_group_id_94350c0c_uniq
	on auth_user_groups (user_id, group_id);

create table captcha_captchastore
(
	id integer not null
		primary key autoincrement,
	challenge varchar(32) not null,
	response varchar(32) not null,
	hashkey varchar(40) not null
		unique,
	expiration datetime not null
);

create table django_content_type
(
	id integer not null
		primary key autoincrement,
	app_label varchar(100) not null,
	model varchar(100) not null
);

create table auth_permission
(
	id integer not null
		primary key autoincrement,
	content_type_id integer not null
		references django_content_type
			deferrable initially deferred,
	codename varchar(100) not null,
	name varchar(255) not null
);

create table auth_group_permissions
(
	id integer not null
		primary key autoincrement,
	group_id integer not null
		references auth_group
			deferrable initially deferred,
	permission_id integer not null
		references auth_permission
			deferrable initially deferred
);

create index auth_group_permissions_group_id_b120cbf9
	on auth_group_permissions (group_id);

create unique index auth_group_permissions_group_id_permission_id_0cd325b0_uniq
	on auth_group_permissions (group_id, permission_id);

create index auth_group_permissions_permission_id_84c5c92e
	on auth_group_permissions (permission_id);

create index auth_permission_content_type_id_2f476e4b
	on auth_permission (content_type_id);

create unique index auth_permission_content_type_id_codename_01ab375a_uniq
	on auth_permission (content_type_id, codename);

create table auth_user_user_permissions
(
	id integer not null
		primary key autoincrement,
	user_id integer not null
		references auth_user
			deferrable initially deferred,
	permission_id integer not null
		references auth_permission
			deferrable initially deferred
);

create index auth_user_user_permissions_permission_id_1fbb5f2c
	on auth_user_user_permissions (permission_id);

create index auth_user_user_permissions_user_id_a95ead1b
	on auth_user_user_permissions (user_id);

create unique index auth_user_user_permissions_user_id_permission_id_14a6b632_uniq
	on auth_user_user_permissions (user_id, permission_id);

create table django_admin_log
(
	id integer not null
		primary key autoincrement,
	action_time datetime not null,
	object_id text,
	object_repr varchar(200) not null,
	change_message text not null,
	content_type_id integer
		references django_content_type
			deferrable initially deferred,
	user_id integer not null
		references auth_user
			deferrable initially deferred,
	action_flag smallint unsigned not null,
	check ("action_flag" >= 0)
);

create index django_admin_log_content_type_id_c4bce8eb
	on django_admin_log (content_type_id);

create index django_admin_log_user_id_c564eba6
	on django_admin_log (user_id);

create unique index django_content_type_app_label_model_76bd3d3b_uniq
	on django_content_type (app_label, model);

create table django_migrations
(
	id integer not null
		primary key autoincrement,
	app varchar(255) not null,
	name varchar(255) not null,
	applied datetime not null
);

create table django_session
(
	session_key varchar(40) not null
		primary key,
	session_data text not null,
	expire_date datetime not null
);

create index django_session_expire_date_a5c62663
	on django_session (expire_date);

