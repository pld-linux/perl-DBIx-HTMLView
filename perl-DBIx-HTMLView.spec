%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	HTMLView
Summary:	DBIx-HTMLView perl module
Summary(pl):	Modu³ perla DBIx-HTMLView
Name:		perl-DBIx-HTMLView
Version:	0.9
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-DBI
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx-HTMLView is a set of modules to handle relational SQL databases
through a DBI interface and create web userinterfaces to them.

%description -l pl
DBIx-HTMLView jest zestawem modu³ów umo¿liwiaj±cych dostêp do
relacyjnych baz danych SQL przy pomocy przegl±darki www, wykorzystuj±c
do tego DBI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz *.cgi
%{perl_sitelib}/DBIx/*.pm
%{perl_sitelib}/DBIx/HTMLView
%{_mandir}/man3/*
