#
# Conditional build:
%bcond_without	tests	# unit tests

%define 	module	isodate
Summary:	An ISO 8601 date/time/duration parser and formater
Summary(pl.UTF-8):	Moduł analizujący i formatujący daty/czas/okresy w formacie ISO 8601
Name:		python3-%{module}
Version:	0.7.2
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.simple/isodate/
Source0:	https://files.pythonhosted.org/packages/source/i/isodate/isodate-%{version}.tar.gz
# Source0-md5:	5ce182fd7f6152cda19ec605b6740687
URL:		https://pypi.org/project/isodate/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools >= 1:61
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements ISO 8601 date, time and duration parsing. The
implementation follows ISO8601:2004 standard, and implements only
date/time representations mentioned in the standard. If something is
not mentioned there, then it is treated as non existent, and not as an
allowed option.

%description -l pl.UTF-8
Ten moduł zawiera implementację analizy daty, czasu i okresów w
formacie ISO 8601. Implementacja jest zgodna ze standardem
ISO8601:2004 i zawiera tylko reprezentacje daty/czasu opisane w
standardzie.

%prep
%setup -q -n isodate-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE README.rst TODO.txt
%dir %{py3_sitescriptdir}/isodate
%{py3_sitescriptdir}/isodate/*.py
%{py3_sitescriptdir}/isodate/__pycache__
%{py3_sitescriptdir}/isodate-%{version}.dist-info
