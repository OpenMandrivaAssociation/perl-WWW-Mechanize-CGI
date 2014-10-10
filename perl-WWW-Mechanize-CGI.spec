%define upstream_name    WWW-Mechanize-CGI
%define upstream_version 0.3

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Use WWW::Mechanize with CGI applications
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

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
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3-4mdv2010.0
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
