use mydatabase;

CREATE INDEX idx_org_name ON organizations(org_name);
CREATE INDEX idx_program_name ON program(program_name);
CREATE INDEX idx_researcher_id ON researcher(researcher_id);
CREATE INDEX idx_phone_number ON phone_number(phone_number);
CREATE INDEX idx_corporate_id ON corporate_member(corporate_id);
CREATE INDEX idx_field_name ON scientific_field(field_name);
CREATE INDEX idx_project_title ON project(project_title);
CREATE INDEX idx_cr_title ON critique(cr_title);
CREATE INDEX idx_report_title ON report(report_title);
  