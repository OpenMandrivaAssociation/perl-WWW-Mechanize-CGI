%define upstream_name    WWW-Mechanize-CGI
Name:		perl-%{upstream_name}
Version:	0.3
Release:	6

Summary:	Use WWW::Mechanize with CGI applications
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/WWW-Mechanize-CGI
Source0:	https://cpan.metacpan.org/authors/id/M/MR/MRAMBERG/WWW-Mechanize-CGI-%{version}.tar.gz

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
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/WWW

%changelog
* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2010.1
+ Revision: 505369
- rebuild using %0.3 Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3-4mdv2010.0
+ Revision: 430656
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.3-3mdv2009.0
+ Revision: 268875
- rebuild early 2009.0 package (before pixel changes)

  + Michael Scherer <misc@mandriva.org>
    - enhance the description

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.3-2mdv2009.0
+ Revision: 213729
- fix dependencies
- import perl-WWW-Mechanize-CGI


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.3-1mdv2009.0
- first mdv release
