Summary:	An HTTP and WebDAV client library
Summary(pl):	Biblioteka kliencka HTTP i WebDAV
Name:		neon
Version:	0.17.2
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Source0:	http://www.webdav.org/neon/%{name}-%{version}.tar.gz
URL:		http://www.webdav.org/neon
BuildRequires:	openssl-devel
BuildRequires:	expat-devel
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

%package	devel
Summary:	Static Libraries and header files for neon
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
#Requires:	%{name} = %{version}

%description	devel
Static libraries and C header files for the neon library.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --with-ssl --enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
[ -d $RPM_BUILD_ROOT] && rm -rf $RPM_BUILD_ROOT;
install -d $RPM_BUILD_ROOT%{_prefix}
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

gzip -9nf AUTHORS BUGS ChangeLog NEWS README THANKS TODO doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS.gz BUGS.gz ChangeLog.gz NEWS.gz README.gz THANKS.gz TODO.gz doc/*
%attr(755,root,root) %{_bindir}/neon-config
%{_libdir}/*.so*

%files devel
%defattr(644,root,root,755)
%{_includedir}/neon
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
