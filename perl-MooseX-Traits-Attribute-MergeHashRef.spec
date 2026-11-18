#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	MooseX
%define	pnam	Traits-Attribute-MergeHashRef
Summary:	Moose::Meta::Attribute::Custom::Trait::MergeHashRef
#Summary(pl.UTF-8):
Name:		perl-MooseX-Traits-Attribute-MergeHashRef
Version:	1.002
Release:	1
License:	bsd
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/P/PE/PERLER/MooseX-Traits-Attribute-MergeHashRef-%{version}.tar.gz
# Source0-md5:	0ceade0624acff9f7a4663adb45cf155
Patch0:		%{name}-moose2.patch
URL:		http://search.cpan.org/dist/MooseX-Traits-Attribute-MergeHashRef/
BuildRequires:	perl-Module-Build >= 0.3601
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Hash-Merge
BuildRequires:	perl-Moose
BuildRequires:	perl-Test-Simple >= 0.92
BuildRequires:	perl-Try-Tiny
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description


# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P 0 -p1

%build
%{__perl} Build.PL \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	destdir=$RPM_BUILD_ROOT

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
