%include	/usr/lib/rpm/macros.perl
Summary:	DBIx-HTMLView perl module
Summary(pl):	Modu³ perla DBIx-HTMLView
Name:		perl-DBIx-HTMLView
Version:	0.6.1
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBIx/DBIx-HTMLView-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-DBI
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
DBIx-HTMLView is a set of modules to handle relational SQL databases through 
a DBI interface and create web userinterfaces to them.

%description -l pl
DBIx-HTMLView jest zestawem modu³ów umo¿liwiaj±cych dostêp do relacyjnych 
baz danych SQL przy pomocy przegl±darki www, wykorzystuj±c do tego DBI.

%prep
%setup -q -n DBIx-HTMLView-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/DBIx/HTMLView
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README TODO NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO,NEWS}.gz *.cgi

%{perl_sitelib}/DBIx/*.pm
%{perl_sitelib}/DBIx/HTMLView
%{perl_sitearch}/auto/DBIx/HTMLView

%{_mandir}/man3/*
