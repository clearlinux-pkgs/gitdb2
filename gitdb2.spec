#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x665F99FA9D99966C (byronimo@gmail.com)
#
Name     : gitdb2
Version  : 2.0.6
Release  : 7
URL      : https://files.pythonhosted.org/packages/c5/62/ed7205331e8d7cc377e2512cb32f8f8f075c0defce767551d0a76e102ce2/gitdb2-2.0.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/c5/62/ed7205331e8d7cc377e2512cb32f8f8f075c0defce767551d0a76e102ce2/gitdb2-2.0.6.tar.gz
Source1 : https://files.pythonhosted.org/packages/c5/62/ed7205331e8d7cc377e2512cb32f8f8f075c0defce767551d0a76e102ce2/gitdb2-2.0.6.tar.gz.asc
Summary  : Git Object Database
Group    : Development/Tools
License  : BSD-3-Clause
Requires: gitdb2-license = %{version}-%{release}
Requires: gitdb2-python = %{version}-%{release}
Requires: gitdb2-python3 = %{version}-%{release}
Requires: smmap2
BuildRequires : buildreq-distutils3
BuildRequires : smmap2

%description
GitDB
=====
GitDB allows you to access bare git repositories for reading and writing. It aims at allowing full access to loose objects as well as packs with performance and scalability in mind. It operates exclusively on streams, allowing to handle large objects with a small memory footprint.

%package license
Summary: license components for the gitdb2 package.
Group: Default

%description license
license components for the gitdb2 package.


%package python
Summary: python components for the gitdb2 package.
Group: Default
Requires: gitdb2-python3 = %{version}-%{release}

%description python
python components for the gitdb2 package.


%package python3
Summary: python3 components for the gitdb2 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the gitdb2 package.


%prep
%setup -q -n gitdb2-2.0.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569779502
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gitdb2
cp LICENSE %{buildroot}/usr/share/package-licenses/gitdb2/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gitdb2/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
