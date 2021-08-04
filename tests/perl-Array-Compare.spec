Name:           perl-Array-Compare
Version:        1.16
Epoch:		1
Release:        1%{?dist}
Summary:        Perl extension for comparing arrays
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Array-Compare/
Source0:        http://www.cpan.org/authors/id/D/DA/DAVECROSS/Array-Compare-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
ExcludeArch:    alpha
ExclusiveArch:  i386 x86_64
BuildRequires:  perl >= 1:5.6.0
BuildRequires:  perl(Module::Build)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
If you have two arrays and you want to know if they are the same or
different, then Array::Compare will be useful to you.

%prep
%setup -q -n Array-Compare-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Aug 19 2008 Dave Cross <dave@mag-sol.com> 1.16-1
- Specfile autogenerated by cpanspec 1.77.
