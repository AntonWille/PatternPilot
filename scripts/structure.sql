SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

-- TABLES

CREATE TABLE public.answers (
    answer_id bigint NOT NULL,
    owner_id character varying,
    owner_display_name character varying,
    question_id bigint NOT NULL,
    body text,
    is_accepted boolean,
    comment_count integer,
    score integer,
    last_activity_date integer,
    creation_date integer
);

CREATE TABLE public.codes (
    id bigint NOT NULL,
    name character varying NOT NULL,
    description text,
    parent_id bigint,
    created_at timestamp(6) without time zone NOT NULL,
    updated_at timestamp(6) without time zone NOT NULL
);

CREATE TABLE public.codes_sentences (
    id bigint NOT NULL,
    code_id bigint,
    sentence_id bigint,
    created_at timestamp(6) without time zone NOT NULL,
    updated_at timestamp(6) without time zone NOT NULL
);

CREATE TABLE public.questions_comments (
    comment_id bigint NOT NULL,
    parent_id integer NOT NULL,
    owner_id character varying,
    owner_display_name character varying,
    body text,
    score integer,
    creation_date integer
);
CREATE TABLE public.answers_comments (
    comment_id bigint NOT NULL,
    parent_id integer NOT NULL,
    owner_id character varying,
    owner_display_name character varying,
    body text,
    score integer,
    creation_date integer
);

CREATE TABLE public.questions (
    question_id bigint NOT NULL,
    title character varying,
    owner_id character varying,
    owner_display_name character varying,
    tags character varying,
    body text,
    is_answered boolean,
    answer_count integer,
    comment_count integer,
    view_count integer,
    score integer,
    link character varying,
    category character varying,
    last_activity_date integer,
    creation_date integer
);

CREATE TABLE public.sentences (
    id bigint NOT NULL,
    post_type character varying NOT NULL,
    post_id bigint NOT NULL,
    sequence_number integer,
    sentence_text text,
    created_at timestamp(6) without time zone NOT NULL,
    updated_at timestamp(6) without time zone NOT NULL
);

-- PRIMARY KEYS

ALTER TABLE ONLY public.answers
    ADD CONSTRAINT answers_pkey PRIMARY KEY (answer_id);

ALTER TABLE ONLY public.codes
    ADD CONSTRAINT codes_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.codes_sentences
    ADD CONSTRAINT codes_sentences_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.questions_comments
    ADD CONSTRAINT questions_comments_pkey PRIMARY KEY (comment_id);

ALTER TABLE ONLY public.answers_comments
    ADD CONSTRAINT answers_comments_pkey PRIMARY KEY (comment_id);

ALTER TABLE ONLY public.questions
    ADD CONSTRAINT questions_pkey PRIMARY KEY (question_id);

ALTER TABLE ONLY public.sentences
    ADD CONSTRAINT sentences_pkey PRIMARY KEY (id);

-- INDEXES

CREATE INDEX index_codes_on_parent_id ON public.codes USING btree (parent_id);

CREATE INDEX index_codes_sentences_on_code_id ON public.codes_sentences USING btree (code_id);

CREATE INDEX index_codes_sentences_on_sentence_id ON public.codes_sentences USING btree (sentence_id);

CREATE INDEX index_comments_on_commentable ON public.comments USING btree (commentable_type, commentable_id);

-- FK_CONSTRAINTS

ALTER TABLE ONLY public.codes
    ADD CONSTRAINT fk_codes_codes FOREIGN KEY (parent_id) REFERENCES public.codes(id) ON DELETE CASCADE;

ALTER TABLE ONLY public.answers
    ADD CONSTRAINT fk_answers_questions FOREIGN KEY (question_id) REFERENCES public.questions(question_id) ON DELETE CASCADE;

ALTER TABLE ONLY public.codes_sentences
    ADD CONSTRAINT fk_codes_sentences_codes FOREIGN KEY (code_id) REFERENCES public.codes(id) ON DELETE CASCADE;

ALTER TABLE ONLY public.codes_sentences
    ADD CONSTRAINT fk_codes_sentences_sentences FOREIGN KEY (sentence_id) REFERENCES public.sentences(id) ON DELETE CASCADE;

ALTER TABLE ONLY public.answers_comments
    ADD CONSTRAINT fk_answers_comments_answers FOREIGN KEY (parent_id) REFERENCES public.answers(answer_id) ON DELETE CASCADE;

ALTER TABLE ONLY public.questions_comments
    ADD CONSTRAINT fk_questions_comments_questions FOREIGN KEY (parent_id) REFERENCES public.questions(question_id) ON DELETE CASCADE;

-- SEARCH_PATH
SET search_path TO "$user", public;


