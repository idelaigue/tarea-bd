PGDMP     (    ,                y         	   postgress    12.6    12.6     *           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            +           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ,           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            -           1262    24597 	   postgress    DATABASE     ?   CREATE DATABASE postgress WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Spanish_Chile.1252' LC_CTYPE = 'Spanish_Chile.1252';
    DROP DATABASE postgress;
                postgres    false            ?            1259    24608    cuenta_bancaria    TABLE     ?   CREATE TABLE public.cuenta_bancaria (
    numero_cuenta integer NOT NULL,
    id_usuario integer NOT NULL,
    balance double precision NOT NULL
);
 #   DROP TABLE public.cuenta_bancaria;
       public         heap    postgres    false            ?            1259    24613    moneda    TABLE     ?   CREATE TABLE public.moneda (
    id integer NOT NULL,
    sigla character varying(10) NOT NULL,
    nombre character varying(80) NOT NULL
);
    DROP TABLE public.moneda;
       public         heap    postgres    false            ?            1259    24598    pais    TABLE     g   CREATE TABLE public.pais (
    cod_pais integer NOT NULL,
    nombre character varying(45) NOT NULL
);
    DROP TABLE public.pais;
       public         heap    postgres    false            ?            1259    24790    precio_moneda    TABLE     ?   CREATE TABLE public.precio_moneda (
    id_moneda integer NOT NULL,
    fecha timestamp without time zone NOT NULL,
    valor double precision NOT NULL
);
 !   DROP TABLE public.precio_moneda;
       public         heap    postgres    false            ?            1259    24630    usuario    TABLE     B  CREATE TABLE public.usuario (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    apellido character varying(50),
    correo character varying(50) NOT NULL,
    "contraseña" character varying(60) NOT NULL,
    pais integer NOT NULL,
    fecha_registro date NOT NULL,
    tipo character varying(15)
);
    DROP TABLE public.usuario;
       public         heap    postgres    false            ?            1259    24628    usuario_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.usuario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.usuario_id_seq;
       public          postgres    false    206            .           0    0    usuario_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.usuario_id_seq OWNED BY public.usuario.id;
          public          postgres    false    205            ?            1259    24636    usuario_tiene_moneda    TABLE     ?   CREATE TABLE public.usuario_tiene_moneda (
    id_usuario integer NOT NULL,
    id_moneda integer NOT NULL,
    balance double precision NOT NULL
);
 (   DROP TABLE public.usuario_tiene_moneda;
       public         heap    postgres    false            ?
           2604    24633 
   usuario id    DEFAULT     h   ALTER TABLE ONLY public.usuario ALTER COLUMN id SET DEFAULT nextval('public.usuario_id_seq'::regclass);
 9   ALTER TABLE public.usuario ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    205    206    206            "          0    24608    cuenta_bancaria 
   TABLE DATA           M   COPY public.cuenta_bancaria (numero_cuenta, id_usuario, balance) FROM stdin;
    public          postgres    false    203   "       #          0    24613    moneda 
   TABLE DATA           3   COPY public.moneda (id, sigla, nombre) FROM stdin;
    public          postgres    false    204   :"       !          0    24598    pais 
   TABLE DATA           0   COPY public.pais (cod_pais, nombre) FROM stdin;
    public          postgres    false    202   ?"       '          0    24790    precio_moneda 
   TABLE DATA           @   COPY public.precio_moneda (id_moneda, fecha, valor) FROM stdin;
    public          postgres    false    208   _#       %          0    24630    usuario 
   TABLE DATA           j   COPY public.usuario (id, nombre, apellido, correo, "contraseña", pais, fecha_registro, tipo) FROM stdin;
    public          postgres    false    206   L*       &          0    24636    usuario_tiene_moneda 
   TABLE DATA           N   COPY public.usuario_tiene_moneda (id_usuario, id_moneda, balance) FROM stdin;
    public          postgres    false    207   ?*       /           0    0    usuario_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.usuario_id_seq', 2, true);
          public          postgres    false    205            ?
           2606    24612 $   cuenta_bancaria cuenta_bancaria_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public.cuenta_bancaria
    ADD CONSTRAINT cuenta_bancaria_pkey PRIMARY KEY (numero_cuenta);
 N   ALTER TABLE ONLY public.cuenta_bancaria DROP CONSTRAINT cuenta_bancaria_pkey;
       public            postgres    false    203            ?
           2606    24617    moneda moneda_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.moneda
    ADD CONSTRAINT moneda_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.moneda DROP CONSTRAINT moneda_pkey;
       public            postgres    false    204            ?
           2606    24602    pais pais_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.pais
    ADD CONSTRAINT pais_pkey PRIMARY KEY (cod_pais);
 8   ALTER TABLE ONLY public.pais DROP CONSTRAINT pais_pkey;
       public            postgres    false    202            ?
           2606    24794     precio_moneda precio_moneda_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.precio_moneda
    ADD CONSTRAINT precio_moneda_pkey PRIMARY KEY (id_moneda, fecha);
 J   ALTER TABLE ONLY public.precio_moneda DROP CONSTRAINT precio_moneda_pkey;
       public            postgres    false    208    208            ?
           2606    24635    usuario usuario_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_pkey;
       public            postgres    false    206            ?
           2606    24649    usuario_tiene_moneda id_moneda    FK CONSTRAINT     ?   ALTER TABLE ONLY public.usuario_tiene_moneda
    ADD CONSTRAINT id_moneda FOREIGN KEY (id_moneda) REFERENCES public.moneda(id) NOT VALID;
 H   ALTER TABLE ONLY public.usuario_tiene_moneda DROP CONSTRAINT id_moneda;
       public          postgres    false    204    2713    207            ?
           2606    24639    usuario_tiene_moneda id_usuario    FK CONSTRAINT     ?   ALTER TABLE ONLY public.usuario_tiene_moneda
    ADD CONSTRAINT id_usuario FOREIGN KEY (id_usuario) REFERENCES public.usuario(id);
 I   ALTER TABLE ONLY public.usuario_tiene_moneda DROP CONSTRAINT id_usuario;
       public          postgres    false    206    207    2715            ?
           2606    24654    cuenta_bancaria id_usuario    FK CONSTRAINT     ?   ALTER TABLE ONLY public.cuenta_bancaria
    ADD CONSTRAINT id_usuario FOREIGN KEY (id_usuario) REFERENCES public.usuario(id) NOT VALID;
 D   ALTER TABLE ONLY public.cuenta_bancaria DROP CONSTRAINT id_usuario;
       public          postgres    false    206    203    2715            ?
           2606    24644    usuario pais    FK CONSTRAINT     w   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT pais FOREIGN KEY (pais) REFERENCES public.pais(cod_pais) NOT VALID;
 6   ALTER TABLE ONLY public.usuario DROP CONSTRAINT pais;
       public          postgres    false    206    2709    202            ?
           2606    24795 *   precio_moneda precio_moneda_id_moneda_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.precio_moneda
    ADD CONSTRAINT precio_moneda_id_moneda_fkey FOREIGN KEY (id_moneda) REFERENCES public.moneda(id);
 T   ALTER TABLE ONLY public.precio_moneda DROP CONSTRAINT precio_moneda_id_moneda_fkey;
       public          postgres    false    208    204    2713            "      x?????? ? ?      #   ?   x?-??
?@???>?O?[g??N`?F?b:#z}??ڝ??#?
??:8O???T?<???f6?^????B???{<
ma???fM???B?m?!2S?~?#?<C???e:!Q????:C???l?Q\?²??T?D??2?kED!?2?      !   t   x???1???p??Ox?. ?DF??V?l?>'tC-4?F??`??U?p?????Y?!??KS?0?EBi????=?[S?coK???#.9O??Fq!&7??3??Y?6׏??"?i?#E      '   ?  x?]X??9{???4????ok???8?????Ec????Mۻ?w/9??5?g۲-???>?O??????~Y??>???w[?v?.W;q?؟^ ?xQװ"?????^2?9?3*??D??pw?2?G??K?E?????7B??ޭ??.Y?D????d ??l\RB?=?:D??vyd?_B?-m]#iY?????;?:^??k?E?R??V?|<?O???$n"?"oA??v\?9kBfc?qIV??HG?zk??|???o?/mx?*w?Hg?????-x맜j??:???q?_????
Ey?փ?G??Q???##??@??(??$?????/??rZ	?ڨ??D,?F?{!c?%O9????k`?1I? a??,?/d\?_???+壂?d?? +)?WCmv??:???E6H%N9?>?"?<??????۝0 'U=a*=?"?????~R ??d?7??{@?Ɉ?A%?"?)??=??KAn?bѥ?@??S??"?d?O??u?S????Kj4?5? B?i:?.bA?i@?[?Ttj?A},?@)??C2?An-?????Bo???$???1??[??~?i??|ҹ?v?0Z ???? ????8???2???ٔ?2??F??1A??{`y??R*?4:~B86?x?t;?	??)?h???E?g??HP????h(?	?
r?,?z/????pQc8W3
ł?+O??o??2;??ٵ@?\(0~9???????8햼pt?юZe?Bi<??????ӟ?n??:c0???Z,?S?)W??	????Z?Ʀ?טW???,!??V\?(?????J?:~?қv&<]qv??k??X??w&?,{??3s;??e0i?; ˧?1???3?}?q?<d?B?cp?p??
???&
?{+?????bЉ?????f????rv???Tt?F???#X6Ǣ?afsp?X?ba??Y?????t7???9%,w??o5)ys??Y 2?S?{?6j??B?n#U^????:[?p;;4????????Ĭ2??o?ܖ???X?H@|?Ap???QȽT?S?N?Z9?8)???K?.??? ?2k\ ƹ?֐2L?ݭ?????]歛A"Ļ?U??U X??Y??9{?"nLd?s?^?UK,>?J??|8?7"?S??!?????>???<????|7?e?Yx?h@BKVtpv{?p??K??`?'?N????9????cоJ???????])?>???P՛?[?a??@?ɝ???S.?ߍ????S??\G??s?M??r?"?8M5?䮋??U?1??N!??l6??CuV???i?8?`??]V?l"*?!ε?V??W??H?)k??)??T?w?ҽA?+?E,?͒t?i?????M????:??? f????̧?7d?H??x2???]???bVY???O???ߖe??S?ԋ?+B?M?E?t??r+?$U??OG3b?U?L>??E?W۲[-???(??f9JF?\?B:?V:w+????q??p??S??_A?n????	???}?????}?%D?=??????/86pk?W??n??B$?ٷ|WO??FUfCw	j]??⸮Tk?S???t????e=B?W~?)N9J ??	??Yr??`m}?]%??+???????;??b؉\EJ4s????*?j???`?'ͽ???`[~1w??W?^>??????????7???V0Y9??[????{?^??0??ֻ??P_P?We????????1??      %   ?   x?3??L?KL?L?tI?I?L/M?̄?@?鹉?9z????*F?*?F*9f?Fn????aI???.9??f~?EŎŅ?!Ɂ?fގ?Fn?Q%%?Q?9????FF??f??Ɯ?ť?E??\1z\\\ R6)      &      x?????? ? ?     