#
# Conditional build:
%bcond_with	apidocs	# API documentation

Summary:	Lightweight C library for storing RDF data in memory
Summary(pl.UTF-8):	Lekka biblioteka C do przechowywania danych RDF w pamięci
Name:		sord
Version:	0.16.12
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.xz
# Source0-md5:	f0fa98fcb0dc24a05eee518d41fae070
URL:		http://drobilla.net/software/sord/
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	serd-devel >= 0.30.9
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%if %{with apidocs}
BuildRequires:	doxygen
%endif
Requires:	serd >= 0.30.9
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
Requires:	serd-devel >= 0.30.9

%description devel
Header files for sord library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki sord.

%prep
%setup -q

%build
%meson build \
	--default-library=shared \
	%{!?with_apidocs:-Ddocs=disabled}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%if %{without apidocs}
# -Ddocs=disabled disables man page installation
install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README.md
%attr(755,root,root) %{_bindir}/sord_validate
%attr(755,root,root) %{_bindir}/sordi
%attr(755,root,root) %{_libdir}/libsord-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsord-0.so.0
%{_mandir}/man1/sord_validate.1*
%{_mandir}/man1/sordi.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsord-0.so
%{_includedir}/sord-0
%{_pkgconfigdir}/sord-0.pc
