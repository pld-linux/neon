#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
%bcond_without	krb		# don't build krb support
#
Summary:	An HTTP and WebDAV client library
Summary(pl):	Biblioteka kliencka HTTP i WebDAV
Name:		neon
Version:	0.26.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.webdav.org/neon/%{name}-%{version}.tar.gz
# Source0-md5:	3bb7a82bddfc1c56d2f9dba849aecd1f
URL:		http://www.webdav.org/neon/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
%{?with_krb:BuildRequires:	heimdal-devel >= 0.7}
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
neon is an HTTP and WebDAV client library, with a C interface.
Featuring:
 - High-level interface to HTTP and WebDAV methods (PUT, GET, HEAD etc).
 - Low-level interface to HTTP request handling, to allow implementing
   new methods easily.
 - HTTP/1.1 and HTTP/1.0 persistent connections.
 - RFC2617 basic and digest authentication (including auth-int,
   md5-sess).
 - Proxy support (including basic/digest authentication).
 - Generic WebDAV 207 XML response handling mechanism.
 - XML parsing using the expat or libxml parsers.
 - Easy generation of error messages from 207 error responses.
 - WebDAV resource manipulation: MOVE, COPY, DELETE, MKCOL.
 - WebDAV metadata support: set and remove properties, query any set of
   properties (PROPPATCH/PROPFIND).

%description -l pl
neon to biblioteka kliencka HTTP i WebDAV z interfejsem w C.
Mo�liwo�ci:
 - wysokopoziomowy interfejs do metod HTTP i WebDAV (PUT, GET, HEAD...),
 - niskopziomowy interfejs to obs�ugi ��da� HTTP pozwalaj�cy �atwo
   implementowa� nowe metody,
 - sta�e po��czenia HTTP/1.1 i HTTP/1.0,
 - autentykacja podstawowa i skr�tem RFC-2617 (auth-int, md5-sess...),
 - obs�uga proxy (w tym autentykacja podstawowa i skr�tem),
 - mechanizm obs�ugi odpowiedzi WebDAV 207 XML,
 - analiza sk�adniowa XML przy pomocy expat lub libxml,
 - proste generowanie komunikat�w b��d�w dla odpowiedzi 207,
 - manipulowanie zasobami WebDAV: MOVE, COPY, DELETE, MKCOL,
 - obs�uga metadanych WebDAV: ustawianie i usuwanie atrybut�w,
   sprawdzanie dowolnego zbioru atrybut�w (PROPPATCH/PROPFIND).

%package devel
Summary:	Header files for neon
Summary(pl):	Pliki nag��wkowe neon
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_krb:Requires:	heimdal-devel >= 0.6-5}
Requires:	libxml2-devel
Requires:	openssl-devel >= 0.9.7c

%description devel
C header files for the neon library.

%description devel -l pl
Pliki nag��wkowe dla biblioteki neon.

%package static
Summary:	Static libraries for neon
Summary(pl):	Biblioteki statyczne neon
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static neon libraries.

%description static -l pl
Statyczne biblioteki neon.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%configure \
	--with-ssl \
	--enable-shared \
	%{!?with_static_libs:--enable-static=no} \
	%{!?with_krb:--without-gssapi} \
	--with-libxml2

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix},%{_mandir}/man1,%{_mandir}/man3}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f doc/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
mv -f doc/man/*.3 $RPM_BUILD_ROOT%{_mandir}/man3

mv $RPM_BUILD_ROOT%{_datadir}/locale/{zh,zh_CN}
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README THANKS TODO doc/*.txt doc/html/*
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/neon-config
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/neon
%{_mandir}/man*/*
%{_pkgconfigdir}/neon.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%endif
