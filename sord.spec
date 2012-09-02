Summary:	Lightweight C library for storing RDF data in memory
Summary(pl.UTF-8):	Lekka biblioteka C do przechowywania danych RDF w pamięci
Name:		sord
Version:	0.10.0
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
# Source0-md5:	ad20105c0cefaed32d59c4665d682cab
URL:		http://drobilla.net/software/sord/
BuildRequires:	libstdc++-devel
BuildRequires:	pcre-devel
BuildRequires:	python
BuildRequires:	serd-devel >= 0.18.0
Requires:	serd >= 0.18.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sord is a lightweight C library for storing RDF data in memory.

%description -l pl.UTF-8
Sort to lekka biblioteka C do przechowywania danych RDF w pamięci.

%package devel
Summary:	Header files for sord library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki sord
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	serd-devel >= 0.18.0

%description devel
Header files for sord library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki sord.

%prep
%setup -q

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

./waf -v

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_bindir}/sord_validate
%attr(755,root,root) %{_bindir}/sordi
%attr(755,root,root) %{_libdir}/libsord-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsord-0.so.0
%{_mandir}/man1/sordi.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsord-0.so
%{_includedir}/sord-0
%{_pkgconfigdir}/sord-0.pc
