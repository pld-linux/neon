Summary:	An HTTP and WebDAV client library
Summary(pl):	Biblioteka kliencka HTTP i WebDAV
Name:		neon
Version:	0.18.1
Release:	2
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	http://www.webdav.org/neon/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.webdav.org/neon/
BuildRequires:	expat-devel
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
neon is an HTTP and WebDAV client library, with a C interface.
Featuring:
 - High-level interface to HTTP and WebDAV methods (PUT, GET, HEAD etc)
 - Low-level interface to HTTP request handling, to allow implementing
   new methods easily.
 - HTTP/1.1 and HTTP/1.0 persistent connections
 - RFC2617 basic and digest authentication (including auth-int,
   md5-sess)
 - Proxy support (including basic/digest authentication)
 - Generic WebDAV 207 XML response handling mechanism
 - XML parsing using the expat or libxml parsers
 - Easy generation of error messages from 207 error responses
 - WebDAV resource manipulation: MOVE, COPY, DELETE, MKCOL.
 - WebDAV metadata support: set and remove properties, query any set of
   properties (PROPPATCH/PROPFIND).

%description -l pl
neon to biblioteka kliencka HTTP i WebDAV z interfejsem w C.
Moøliwo∂ci:
 - wysokopoziomowy interfejs do metod HTTP i WebDAV (PUT, GET, HEAD...)
 - niskopziomowy interfejs to obs≥ugi ø±daÒ HTTP pozwalaj±cy ≥atwo
   implementowaÊ nowe metody
 - sta≥e po≥±czenia HTTP/1.1 i HTTP/1.0
 - autentykacja podstawowa i skrÛtem RFC-2617 (auth-int, md5-sess...)
 - obs≥uga proxy (w tym autentykacja podstawowa i skrÛtem)
 - mechanizm obs≥ugi odpowiedzi WebDAV 207 XML
 - parsowanie XML przy momocy expat lub libxml
 - proste generowanie komunikatÛw b≥ÍdÛw dla odpowiedzi 207
 - manipulowanie zasobami WebDAV: MOVE, COPY, DELETE, MKCOL
 - obs≥uga metadanych WebDAV: ustawianie i usuwanie atrybutÛw,
   sprawdzanie dowolnego zbioru atrybutÛw (PROPPATCH/PROPFIND).

%package devel
Summary:	Header files for neon
Summary(pl):	Pliki nag≥Ûwkowe neon
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
C header files for the neon library.

%description devel -l pl
Pliki nag≥Ûwkowe dla biblioteki neon.

%package static
Summary:	Static libraries for neon
Summary(pl):	Biblioteki statyczne neon
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static neon libraries.

%description static -l pl
Statyczne biblioteki neon.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--with-ssl \
	--enable-shared \
	--with-libxml2

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix},%{_mandir}/man1,%{_mandir}/man3}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

mv	doc/*.1	$RPM_BUILD_ROOT/%{_mandir}/man1/
mv	doc/*.3	$RPM_BUILD_ROOT/%{_mandir}/man3/

gzip -9nf AUTHORS BUGS ChangeLog NEWS README THANKS TODO \
	doc/*.txt doc/*.ps doc/*.pdf doc/*.sgml doc/*.xml

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz doc/html/*
%attr(755,root,root) %{_bindir}/neon-config
%attr(755,root,root) %{_libdir}/*.so*
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/neon
%{_includedir}/neon/*
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
