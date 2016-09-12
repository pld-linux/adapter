Summary:	Adapt RPM .spec files to PLD Linux coding standard
Name:		adapter
Version:	1.514
Release:	1
License:	GPL
Group:		Applications/File
Source0:	adapter.awk
Source1:	adapter.sh
BuildRequires:	sed >= 4.0
Requires:	gawk >= 3.1.7
Conflicts:	rpm-build-tools < 4.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir	%{_prefix}/lib

%description
adapter adapts RPM .spec files for PLD Linux coding standard.

%prep
%setup -qcT
cp -p %{SOURCE0} %{SOURCE1} .

%{__sed} -i -e 's,^adapter=.*/adapter.awk,adapter=%{_libdir}/adapter.awk,' adapter.sh

%{__sed} -i -e '/^VERSION=/s,\([^/]\+\)/.*",\1-RELEASE",' adapter.sh
%{__sed} -i -e '/\tRCSID =/,/^\trev =/d;/\tVERSION = /s,\([^/]\+\)/.*,\1-RELEASE",' adapter.awk

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}
cp -p adapter.awk $RPM_BUILD_ROOT%{_libdir}/adapter.awk
install -p adapter.sh $RPM_BUILD_ROOT%{_bindir}/adapter

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/adapter
%{_libdir}/adapter.awk
