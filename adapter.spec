Summary:	Adapt RPM .spec files to PLD Linux coding standard
Summary(pl.UTF-8):	Adaptowanie plików .spec pakietów RPM do standardu kodowania PLD Linuksa
Name:		adapter
Version:	1.516
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

%description -l pl.UTF-8
adapter adaptuje pliki .spec pakietów RPM do standardu kodowania PLD
Linuksa.

%prep
%setup -qcT
cp -p %{SOURCE0} %{SOURCE1} .

%{__sed} -i -e 's,^adapter=.*/adapter.awk,adapter=%{_libdir}/adapter.awk,' adapter.sh

%build
die() { echo >&2 "$*"; exit 1; }
for f in adapter.sh adapter.awk; do
	v=$(sed -rne 's/.*VERSION="([^"]+)".*/\1/p' $f)
	if [ "$v" != "%{version}" ]; then
		die "VERSION not %{version} in $f"
	fi
done

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
