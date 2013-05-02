#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	static_libs	# don't build static libraries
%bcond_without	kerberos5	# don't build Kerberos V support
%bcond_without	libproxy	# don't build libproxy support
%bcond_without	pakchois	# don't build pakchois-based PKCS#11 support

Summary:	An HTTP and WebDAV client library
Summary(pl.UTF-8):	Biblioteka kliencka HTTP i WebDAV
Name:		neon
Version:	0.29.6
Release:	8
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.webdav.org/neon/%{name}-%{version}.tar.gz
# Source0-md5:	591e0c82e6979e7e615211b386b8f6bc
URL:		http://www.webdav.org/neon/
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake
%{?with_kerberos5:BuildRequires:	heimdal-devel}
%{?with_libproxy:BuildRequires:	libproxy-devel}
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel >= 0.9.7d
%{?with_pakchois:BuildRequires:	pakchois-devel}
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
%requires_eq_to	openssl openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
neon is an HTTP and WebDAV client library, with a C interface.
Featuring:
 - High-level interface to HTTP and WebDAV methods (PUT, GET, HEAD
   etc).
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

%description -l pl.UTF-8
neon to biblioteka kliencka HTTP i WebDAV z interfejsem w C.
Możliwości:
 - wysokopoziomowy interfejs do metod HTTP i WebDAV (PUT, GET,
   HEAD...),
 - niskopoziomowy interfejs do obsługi żądań HTTP pozwalający łatwo
   implementować nowe metody,
 - stałe połączenia HTTP/1.1 i HTTP/1.0,
 - uwierzytelnianie podstawowe (basic) i skrótem RFC-2617 (auth-int,
   md5-sess...),
 - obsługa proxy (w tym uwierzytelnianie podstawowe i skrótem),
 - mechanizm obsługi odpowiedzi WebDAV 207 XML,
 - analiza składniowa XML przy pomocy expat lub libxml,
 - proste generowanie komunikatów błędów dla odpowiedzi 207,
 - manipulowanie zasobami WebDAV: MOVE, COPY, DELETE, MKCOL,
 - obsługa metadanych WebDAV: ustawianie i usuwanie atrybutów,
   sprawdzanie dowolnego zbioru atrybutów (PROPPATCH/PROPFIND).

%package devel
Summary:	Header files for neon
Summary(pl.UTF-8):	Pliki nagłówkowe neon
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_kerberos5:Requires:	heimdal-devel}
%{?with_libproxy:Requires:	libproxy-devel}
%{?with_pakchois:Requires:	pakchois-devel}
Requires:	libxml2-devel
Requires:	openssl-devel >= 0.9.7c

%description devel
C header files for the neon library.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki neon.

%package static
Summary:	Static libraries for neon
Summary(pl.UTF-8):	Biblioteki statyczne neon
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static neon libraries.

%description static -l pl.UTF-8
Statyczne biblioteki neon.

%package apidocs
Summary:	neon API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki neon
Group:		Documentation

%description apidocs
API and internal documentation for neon library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki neon.

%prep
%setup -q

%build
%{__libtoolize} --install
%{__aclocal} -I macros
%{__autoconf}
%configure \
	--with-ssl=openssl \
	--enable-threadsafe-ssl=posix \
	--enable-shared \
	--with-ca-bundle=/etc/certs/ca-certificates.crt \
	--with%{!?with_pakchois:out}-pakchois \
	%{!?with_static_libs:--disable-static} \
	%{!?with_kerberos5:--without-gssapi} \
	%{!?with_libproxy:--without-libproxy} \
	--with-libxml2

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/libneon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libneon.so.27

%files devel
%defattr(644,root,root,755)
%doc doc/*.txt
%attr(755,root,root) %{_bindir}/neon-config
%attr(755,root,root) %{_libdir}/libneon.so
%{_includedir}/neon
%{_pkgconfigdir}/neon.pc
%{_mandir}/man1/neon-config.1*
%{_mandir}/man3/ne_*.3*
%{_mandir}/man3/neon.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libneon.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
%endif
