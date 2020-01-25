#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	MooseX
%define	pnam	Traits-Attribute-MergeHashRef
Summary:	Moose::Meta::Attribute::Custom::Trait::MergeHashRef
#Summary(pl.UTF-8):
Name:		perl-MooseX-Traits-Attribute-MergeHashRef
Version:	1.000
Release:	3
License:	bsd
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PERLER/MooseX-Traits-Attribute-MergeHashRef-%{version}.tar.gz
# Source0-md5:	631514d096b5ee38bbe44719641765d2
URL:		http://search.cpan.org/dist/MooseX-Traits-Attribute-MergeHashRef/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-File-Find-Rule
BuildRequires:	perl-Hash-Merge
BuildRequires:	perl-Moose
BuildRequires:	perl-Test-Simple >= 0.92
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description


# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{perl_vendorlib}/MooseX/Traits
%dir %{perl_vendorlib}/MooseX/Traits/Attribute
%{perl_vendorlib}/MooseX/Traits/Attribute/*.pm
%dir %{perl_vendorlib}/Moose
%dir %{perl_vendorlib}/Moose/Meta
%dir %{perl_vendorlib}/Moose/Meta/Attribute
%dir %{perl_vendorlib}/Moose/Meta/Attribute/Custom
%dir %{perl_vendorlib}/Moose/Meta/Attribute/Custom/Trait
%{perl_vendorlib}/Moose/Meta/Attribute/Custom/Trait/MergeHashRef.pm

%{_mandir}/man3/*
