%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	HTMLView
Summary:	DBIx::HTMLView perl module
Summary(pl):	Modu³ perla DBIx::HTMLView
Name:		perl-DBIx-HTMLView
Version:	0.9
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildRequires:	perl-DBI
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::HTMLView is a set of modules to handle relational SQL databases
through a DBI interface and create web userinterfaces to them.

%description -l pl
DBIx::HTMLView jest zestawem modu³ów umo¿liwiaj±cych dostêp do
relacyjnych baz danych SQL przy pomocy przegl±darki www, wykorzystuj±c
do tego DBI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install *.cgi $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO NEWS
%{perl_vendorlib}/DBIx/*.pm
%{perl_vendorlib}/DBIx/HTMLView
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
