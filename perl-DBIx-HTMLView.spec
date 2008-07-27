#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# fail on database access when DBI::mysql present
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBIx
%define		pnam	HTMLView
Summary:	DBIx::HTMLView - handling DBI relation databases and web interfaces
Summary(pl.UTF-8):	DBIx::HTMLView - obsługa relacyjnych baz danych DBI i interfejsów WWW
Name:		perl-DBIx-HTMLView
Version:	0.9
Release:	7
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5dabf6cdfc15e60155d4b955ccb18ae3
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-DBI
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::HTMLView is a set of modules to handle relational SQL databases
through a DBI interface and create web userinterfaces to them.

%description -l pl.UTF-8
DBIx::HTMLView jest zestawem modułów umożliwiających dostęp do
relacyjnych baz danych SQL przy pomocy przeglądarki WWW, wykorzystując
do tego DBI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
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
