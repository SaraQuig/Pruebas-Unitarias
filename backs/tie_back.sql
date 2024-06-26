PGDMP  "    9        
        |            DDBB    15.7    16.3                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            	           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            
           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16398    DDBB    DATABASE     {   CREATE DATABASE "DDBB" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Ecuador.1252';
    DROP DATABASE "DDBB";
                postgres    false                       0    0    DATABASE "DDBB"    COMMENT     2   COMMENT ON DATABASE "DDBB" IS 'DATABASE OF SHOP';
                   postgres    false    3339            �            1259    16415    products    TABLE     �   CREATE TABLE public.products (
    id_pro integer NOT NULL,
    name_pro text NOT NULL,
    descrip_pro text NOT NULL,
    cant integer NOT NULL,
    precio double precision NOT NULL,
    oferta boolean
);
    DROP TABLE public.products;
       public         heap    postgres    false            �            1259    16414    products_id_pro_seq    SEQUENCE     �   CREATE SEQUENCE public.products_id_pro_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.products_id_pro_seq;
       public          postgres    false    217                       0    0    products_id_pro_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.products_id_pro_seq OWNED BY public.products.id_pro;
          public          postgres    false    216            �            1259    16400    user    TABLE     �   CREATE TABLE public."user" (
    id integer NOT NULL,
    username text NOT NULL,
    "email " text NOT NULL,
    "age " integer
);
    DROP TABLE public."user";
       public         heap    postgres    false            �            1259    16399    user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.user_id_seq;
       public          postgres    false    215                       0    0    user_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;
          public          postgres    false    214            k           2604    16418    products id_pro    DEFAULT     r   ALTER TABLE ONLY public.products ALTER COLUMN id_pro SET DEFAULT nextval('public.products_id_pro_seq'::regclass);
 >   ALTER TABLE public.products ALTER COLUMN id_pro DROP DEFAULT;
       public          postgres    false    217    216    217            j           2604    16403    user id    DEFAULT     d   ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);
 8   ALTER TABLE public."user" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215                      0    16415    products 
   TABLE DATA           W   COPY public.products (id_pro, name_pro, descrip_pro, cant, precio, oferta) FROM stdin;
    public          postgres    false    217   :                 0    16400    user 
   TABLE DATA           @   COPY public."user" (id, username, "email ", "age ") FROM stdin;
    public          postgres    false    215   W                  0    0    products_id_pro_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.products_id_pro_seq', 1, false);
          public          postgres    false    216                       0    0    user_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.user_id_seq', 1, false);
          public          postgres    false    214            m           2606    16411    user email_unique  
   CONSTRAINT     U   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT "email_unique " UNIQUE ("email ");
 @   ALTER TABLE ONLY public."user" DROP CONSTRAINT "email_unique ";
       public            postgres    false    215            s           2606    16422    products products_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id_pro);
 @   ALTER TABLE ONLY public.products DROP CONSTRAINT products_pkey;
       public            postgres    false    217            o           2606    16413    user user_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_pkey;
       public            postgres    false    215            q           2606    16409    user username_unique  
   CONSTRAINT     X   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT "username_unique " UNIQUE (username);
 C   ALTER TABLE ONLY public."user" DROP CONSTRAINT "username_unique ";
       public            postgres    false    215                  x������ � �            x������ � �     