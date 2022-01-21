BEGIN;
--
-- Create model Document
--
CREATE TABLE "report_app_document" ("id" bigserial NOT NULL PRIMARY KEY, "description" varchar(255) NOT NULL, "upload_at" timestamp with time zone NOT NULL, "document" varchar(100) NOT NULL);
--
-- Create model Document2
--
CREATE TABLE "report_app_document2" ("id" bigserial NOT NULL PRIMARY KEY, "description" varchar(255) NOT NULL, "upload_at" timestamp with time zone NOT NULL, "document" varchar(100) NOT NULL);
--
-- Create model Problem
--
CREATE TABLE "report_app_problem" ("id" bigserial NOT NULL PRIMARY KEY, "title" varchar(250) NOT NULL, "id_problem" integer NOT NULL, "data_problem" timestamp with time zone NOT NULL, "description_problem" text NOT NULL);
--
-- Create model ReestrUsers
--
CREATE TABLE "report_app_reestrusers" ("id" bigserial NOT NULL PRIMARY KEY, "name_m_surname" varchar(5) NOT NULL, "name_pc" varchar(25) NOT NULL, "type_pc" varchar(1) NOT NULL, "department" varchar(1) NOT NULL, "position_pers" varchar(5) NOT NULL, "type_equip" varchar(2) NOT NULL, "inv_num_notebook" varchar(2) NOT NULL, "inv_num_thin_client" varchar(2) NOT NULL, "inv_num_main_equip" varchar(2) NOT NULL, "type_processor" varchar(1) NOT NULL, "ram" integer NOT NULL, "type_video" varchar(1) NOT NULL, "sound_devices" varchar(1) NOT NULL, "inv_num_sound_speakers" varchar(2) NOT NULL, "serial_num_monitor" varchar(70) NOT NULL, "inv_num_monitor" varchar(2) NOT NULL, "diagonal_monitor" integer NOT NULL, "num_monitor" integer NOT NULL, "power_filter" varchar(1) NOT NULL, "local_printer" varchar(1) NOT NULL, "inv_num_printer" varchar(2) NOT NULL, "webcam" varchar(1) NOT NULL, "inv_num_webcam" varchar(2) NOT NULL, "other_devices" varchar(2) NOT NULL, "inv_num_other_devices" integer NULL, "other_devices2" varchar(2) NOT NULL, "inv_num_other_devices2" integer NULL, "ups" varchar(1) NOT NULL, "inv_num_ups" varchar(2) NOT NULL, "type_os" varchar(1) NOT NULL, "mac_addresses" varchar(5) NOT NULL, "brand_phone" varchar(1) NOT NULL, "inv_num_phone" varchar(2) NOT NULL, "number_phone" integer NULL);
--
-- Create index report_app__title_c13d62_idx on field(s) title, description_problem of model problem
--
CREATE INDEX "report_app__title_c13d62_idx" ON "report_app_problem" ("title", "description_problem");
--
-- Create index title_idx on field(s) title of model problem
--
CREATE INDEX "title_idx" ON "report_app_problem" ("title");
COMMIT;
