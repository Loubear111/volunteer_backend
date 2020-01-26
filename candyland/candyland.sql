DROP TABLE user;
DROP TABLE event;
DROP TABLE organization;
DROP TABLE event_user_junction;

CREATE TABLE user (
	username character(100),
	name character(100),
	points integer,
	location character(1000),
	constraint user_pkey PRIMARY KEY (username)
);

CREATE TABLE event (
	location character(1000),
	num_people integer,
	pph integer,
	start_time DATETIME,
	end_time DATETIME,
	name character(1000),
	eid integer,
	host_org character(1000),
	constraint event_pkey PRIMARY KEY (eid),
	constraint organization_fkey FOREIGN KEY (host_org) REFERENCES organization (username)
);

CREATE TABLE organization (
	name character(1000),
	username character(1000),
	location character(1000),
	constraint organization_pkey PRIMARY KEY (username)
);

CREATE TABLE event_user_junction (
	username character(100),
	eid integer,
	constraint event_user_pkey PRIMARY KEY (username,eid),
	constraint event_fkey FOREIGN KEY (eid) REFERENCES event (eid),
	constraint user_fkey FOREIGN KEY (username) REFERENCES user (username)
);
