%define upstream_name    WWW-Mechanize-CGI
%define upstream_version 0.3
Name:		perl-%{upstream_name}
Version:	0.3
Release:	12

Summary:	Use WWW::Mechanize with CGI applications
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/WWW-Mechanize-CGI
Source0:	https://cpan.metacpan.org/authors/id/M/MR/MRAMBERG/WWW-Mechanize-CGI-0.3.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(HTTP::Request::AsCGI)
BuildRequires:	perl(IO::Pipe)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(WWW::Mechanize)

BuildArch:	noarch
Requires:	perl(Class::Accessor::Fast)

%description
Provides a convenient way of using CGI applications with the WWW::Mechanize, 
without setting a webrowser.

%prep
%setup -q -n WWW-Mechanize-CGI-0.3

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test || :

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/WWW

