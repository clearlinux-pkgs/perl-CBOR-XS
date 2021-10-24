#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-CBOR-XS
Version  : 1.85
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/CBOR-XS-1.85.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/CBOR-XS-1.85.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : GPL-3.0
Requires: perl-CBOR-XS-license = %{version}-%{release}
Requires: perl-CBOR-XS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Canary::Stability)
BuildRequires : perl(Types::Serialiser)
BuildRequires : perl(common::sense)

%description
NAME
CBOR::XS - Concise Binary Object Representation (CBOR, RFC7049)
SYNOPSIS
use CBOR::XS;

%package dev
Summary: dev components for the perl-CBOR-XS package.
Group: Development
Provides: perl-CBOR-XS-devel = %{version}-%{release}
Requires: perl-CBOR-XS = %{version}-%{release}

%description dev
dev components for the perl-CBOR-XS package.


%package license
Summary: license components for the perl-CBOR-XS package.
Group: Default

%description license
license components for the perl-CBOR-XS package.


%package perl
Summary: perl components for the perl-CBOR-XS package.
Group: Default
Requires: perl-CBOR-XS = %{version}-%{release}

%description perl
perl components for the perl-CBOR-XS package.


%prep
%setup -q -n CBOR-XS-1.85
cd %{_builddir}/CBOR-XS-1.85

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-CBOR-XS
cp %{_builddir}/CBOR-XS-1.85/COPYING %{buildroot}/usr/share/package-licenses/perl-CBOR-XS/8624bcdae55baeef00cd11d5dfcfa60f68710a02
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/CBOR::XS.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-CBOR-XS/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/CBOR/XS.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/CBOR/XS/XS.so
