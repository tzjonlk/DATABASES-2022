DROP SCHEMA IF EXISTS mydatabase;
CREATE SCHEMA mydatabase;
USE mydatabase;



    CREATE TABLE organizations(
        org_name VARCHAR(50) NOT NULL,
        sorthand VARCHAR(25) NOT NULL,
        postcode INT UNSIGNED NOT NULL,
        street VARCHAR(20) NOT NULL,
        str_number INT UNSIGNED NOT NULL,
        city VARCHAR(20) NOT NULL,
        PRIMARY KEY (org_name)
    );
CREATE TABLE program(
    program_name VARCHAR(20) NOT NULL,
    pr_address VARCHAR(20) NOT NULL,
    PRIMARY KEY (program_name)
    );

CREATE TABLE research_center(
    org_name VARCHAR(50) NOT NULL,
    apart_budget INT UNSIGNED, 
    private_budget INT UNSIGNED,
    PRIMARY KEY (org_name),
    FOREIGN KEY (org_name) REFERENCES organizations(org_name)
);

CREATE TABLE company(
    org_name VARCHAR(50) NOT NULL,
    private_fund INT UNSIGNED,
    PRIMARY KEY (org_name),
    FOREIGN KEY (org_name) REFERENCES organizations(org_name)
);
CREATE TABLE university(
    org_name VARCHAR(50) NOT NULL,
    apart_budget INT UNSIGNED, 
    PRIMARY KEY (org_name),
    FOREIGN KEY (org_name) REFERENCES organizations(org_name)
);

CREATE TABLE researcher(
  researcher_id INT UNSIGNED NOT NULL,
  rfirst_name VARCHAR(15) NOT NULL,
  rlast_name VARCHAR(15) NOT NULL,
  date_of_birth DATE,
  sex VARCHAR(1), 
  PRIMARY KEY (researcher_id));

CREATE TABLE phone_number(
	phone_number VARCHAR(10) NOT NULL,
	org_name VARCHAR(50) NOT NULL,
	PRIMARY KEY(phone_number, org_name),
	FOREIGN KEY(org_name) REFERENCES organizations(org_name)
  );

  CREATE TABLE corporate_member(
      corporate_id INT UNSIGNED NOT NULL,
      cfirst_name VARCHAR(15) NOT NULL,
      clast_name VARCHAR(15) NOT NULL,
      PRIMARY KEY(corporate_id)
  );

  CREATE TABLE scientific_field(
      field_name VARCHAR(30),
      PRIMARY KEY(field_name)
  ) ;

CREATE TABLE project(
    project_title VARCHAR(50) NOT NULL,
    grant_amount INT UNSIGNED NOT NULL ,
    starting_date DATE,
    ending_date DATE,
    project_abstract VARCHAR(255) NOT NULL,
    corporate_id INT UNSIGNED NOT NULL,
    org_name VARCHAR(50) NOT NULL,
    researcher_id INT UNSIGNED NOT NULL,
    field_name VARCHAR(30),
    program_name VARCHAR(20),
    PRIMARY KEY (project_title, researcher_id),
    FOREIGN KEY (corporate_id) REFERENCES corporate_member(corporate_id),
    FOREIGN KEY (org_name) REFERENCES organizations(org_name),
    FOREIGN KEY (researcher_id) REFERENCES researcher (researcher_id),
    FOREIGN KEY (field_name) REFERENCES  scientific_field (field_name),
    FOREIGN KEY (program_name) REFERENCES program(program_name));


 CREATE TABLE critique(
      cr_title VARCHAR(50) NOT NULL,
      grade INT UNSIGNED NOT NULL,
      cr_date DATE,
      project_title VARCHAR(50) NOT NULL,
      PRIMARY KEY (cr_title),
      FOREIGN KEY (project_title) REFERENCES project(project_title)

  );

  CREATE TABLE report(
      report_title VARCHAR(50), -- NOT NULL,
      report_abstract VARCHAR(255),  -- NOT NULL,
      report_date DATE,
      project_title VARCHAR(50), -- NOT NULL,
      -- PRIMARY KEY (report_title,report_abstract,report_date,project_title),
      FOREIGN KEY (project_title) REFERENCES project(project_title)

  );
  
  
  