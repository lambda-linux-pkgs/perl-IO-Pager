%define _buildid .2

Name:           perl-IO-Pager
Version:        0.31
Release:        1%{?_buildid}%{?dist}
Summary:        Select a pager and pipe text to it if destination is a TTY
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IO-Pager/
Source0:        http://cpan.metacpan.org//authors/id/J/JP/JPIERCE/IO-Pager-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Config)
BuildRequires:  perl(Env)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Test::More)
Requires:       perl(Config)
Requires:       perl(File::Which)
Requires:       perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

IO::Pager can be used to locate an available pager and set the PAGER
environment variable (see "NOTES"). It is also a factory for creating I/O
objects such as IO::Pager::Buffered and IO::Pager::Unbuffered.

%prep
%setup -q -n IO-Pager-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 31 2014 Rajiv M Ranganath <rajiv.ranganath@atihita.com> 0.31-1
- Adapt for AL/LL
- Add package support URL
- Update spec file
- Import `IO-Pager-0.31.tgz`
- Import spec file

* Thu Aug 02 2012 David E. Wheeler <david.wheeler@iovation.com> 0.24-1
- Specfile autogenerated by cpanspec 1.78.
