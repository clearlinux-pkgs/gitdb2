#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x665F99FA9D99966C (byronimo@gmail.com)
#
Name     : gitdb2
Version  : 2.0.5
Release  : 2
URL      : https://files.pythonhosted.org/packages/c4/5c/579abccd59187eaf6b3c8a4a6ecd86fce1dfd818155bfe4c52ac28dca6b7/gitdb2-2.0.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/c4/5c/579abccd59187eaf6b3c8a4a6ecd86fce1dfd818155bfe4c52ac28dca6b7/gitdb2-2.0.5.tar.gz
Source99 : https://files.pythonhosted.org/packages/c4/5c/579abccd59187eaf6b3c8a4a6ecd86fce1dfd818155bfe4c52ac28dca6b7/gitdb2-2.0.5.tar.gz.asc
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
%setup -q -n gitdb2-2.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539440293
python3 setup.py build

%install
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
