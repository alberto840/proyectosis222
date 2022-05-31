-- Database: neurolap

-- DROP DATABASE IF EXISTS neurolap;

CREATE DATABASE neurolap
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Spain.1252'
    LC_CTYPE = 'Spanish_Spain.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
	
-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-05-31 14:18:46.249

-- tables
-- Table: condicion_medica
CREATE TABLE condicion_medica (
    condicion_medica_id int  NOT NULL,
    enfermedad varchar(300)  NOT NULL,
    medicacion varchar(30)  NOT NULL,
    fecha_inicio date  NOT NULL,
    paciente_paciente_id int  NOT NULL,
    CONSTRAINT condicion_medica_pk PRIMARY KEY (condicion_medica_id)
);

-- Table: encuesta
CREATE TABLE encuesta (
    gds_id int  NOT NULL,
    pregunta varchar(200)  NOT NULL,
    respuesta varchar(200)  NOT NULL,
    fecha timestamp  NOT NULL,
    tipo varchar(30)  NOT NULL,
    paciente_paciente_id int  NOT NULL,
    personal_personal_id int  NOT NULL,
    CONSTRAINT encuesta_pk PRIMARY KEY (gds_id)
);

-- Table: hijo
CREATE TABLE hijo (
    discriminator int  NOT NULL,
    hijo_id int  NOT NULL,
    paciente_paciente_id int  NOT NULL,
    persona_id int  NULL,
    ci int  NULL,
    nombre_completo varchar(50)  NULL,
    fecha_nacimiento varchar(30)  NULL,
    celular int  NULL,
    email varchar(30)  NULL,
    gÃ©nero varchar(30)  NULL,
    CONSTRAINT hijo_pk PRIMARY KEY (hijo_id)
);

-- Table: idioma
CREATE TABLE idioma (
    idioma_id int  NOT NULL,
    idioma varchar(30)  NOT NULL,
    tipo varchar(30)  NOT NULL,
    paciente_paciente_id int  NOT NULL,
    CONSTRAINT idioma_pk PRIMARY KEY (idioma_id)
);

-- Table: paciente
CREATE TABLE paciente (
    paciente_id int  NOT NULL,
    profesion varchar(30)  NOT NULL,
    estado_civil varchar(30)  NOT NULL,
    grado_instruccion varchar(30)  NOT NULL,
    estado_salud varchar(30)  NOT NULL,
    observaciones varchar(1000)  NOT NULL,
    telefono int  NOT NULL,
    direccion varchar(100)  NOT NULL,
    puntaje_minimental int  NOT NULL,
    medicacion varchar(100)  NOT NULL,
    CONSTRAINT paciente_pk PRIMARY KEY (paciente_id)
);

-- Table: permiso
CREATE TABLE permiso (
    permisos_id varchar(100)  NOT NULL,
    llave varchar(50)  NOT NULL,
    personal_personal_id int  NOT NULL,
    CONSTRAINT permiso_pk PRIMARY KEY (permisos_id)
);

-- Table: personal
CREATE TABLE personal (
    personal_id int  NOT NULL,
    especialidad varchar(30)  NOT NULL,
    cargo varchar(30)  NOT NULL,
    usuario varchar(30)  NOT NULL,
    password varchar(30)  NOT NULL,
    tipo varchar(30)  NOT NULL,
    paciente_paciente_id int  NOT NULL,
    CONSTRAINT personal_pk PRIMARY KEY (personal_id)
);

-- Table: referencia_contacto
CREATE TABLE referencia_contacto (
    referencia_contacto_id int  NOT NULL,
    nombre_contacto varchar(50)  NOT NULL,
    telefono_contacto int  NOT NULL,
    paciente_paciente_id int  NOT NULL,
    CONSTRAINT referencia_contacto_pk PRIMARY KEY (referencia_contacto_id)
);

-- Table: rol
CREATE TABLE rol (
    rol_id int  NOT NULL,
    descripcion varchar(50)  NOT NULL,
    observacion varchar(100)  NOT NULL,
    estado int  NOT NULL,
    personal_personal_id int  NOT NULL,
    CONSTRAINT rol_pk PRIMARY KEY (rol_id)
);

-- foreign keys
-- Reference: condicion_medica_paciente (table: condicion_medica)
ALTER TABLE condicion_medica ADD CONSTRAINT condicion_medica_paciente
    FOREIGN KEY (paciente_paciente_id)
    REFERENCES paciente (paciente_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: contacto_paciente (table: referencia_contacto)
ALTER TABLE referencia_contacto ADD CONSTRAINT contacto_paciente
    FOREIGN KEY (paciente_paciente_id)
    REFERENCES paciente (paciente_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: encuesta_paciente (table: encuesta)
ALTER TABLE encuesta ADD CONSTRAINT encuesta_paciente
    FOREIGN KEY (paciente_paciente_id)
    REFERENCES paciente (paciente_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: encuesta_personal (table: encuesta)
ALTER TABLE encuesta ADD CONSTRAINT encuesta_personal
    FOREIGN KEY (personal_personal_id)
    REFERENCES personal (personal_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: hijo_paciente (table: hijo)
ALTER TABLE hijo ADD CONSTRAINT hijo_paciente
    FOREIGN KEY (paciente_paciente_id)
    REFERENCES paciente (paciente_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: idiomas_paciente (table: idioma)
ALTER TABLE idioma ADD CONSTRAINT idiomas_paciente
    FOREIGN KEY (paciente_paciente_id)
    REFERENCES paciente (paciente_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: permiso_personal (table: permiso)
ALTER TABLE permiso ADD CONSTRAINT permiso_personal
    FOREIGN KEY (personal_personal_id)
    REFERENCES personal (personal_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: personal_paciente (table: personal)
ALTER TABLE personal ADD CONSTRAINT personal_paciente
    FOREIGN KEY (paciente_paciente_id)
    REFERENCES paciente (paciente_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: rol_personal (table: rol)
ALTER TABLE rol ADD CONSTRAINT rol_personal
    FOREIGN KEY (personal_personal_id)
    REFERENCES personal (personal_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

