%define	pdir	DBIx
%define	pnam	HTMLView
%include	/usr/lib/rpm/macros.perl
Summary:	DBIx-HTMLView perl module
Summary(pl):	Modu� perla DBIx-HTMLView
Name:		perl-DBIx-HTMLView
Version:	0.9
Release:	3

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
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
DBIx-HTMLView jest zestawem modu��w umo�liwiaj�cych dost�p do
relacyjnych baz danych SQL przy pomocy przegl�darki www, wykorzystuj�c
do tego DBI.

%prep
%setup -q -n DBIx-HTMLView-%{version}

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
