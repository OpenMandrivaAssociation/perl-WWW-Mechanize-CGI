%define upstream_name    WWW-Mechanize-CGI
%define upstream_version 0.3

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Use WWW::Mechanize with CGI applications
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(File::Spec)
BuildRequires: perl(HTTP::Request::AsCGI)
BuildRequires: perl(IO::Pipe)
BuildRequires: perl(Test::More)
BuildRequires: perl(WWW::Mechanize)

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

Requires: perl(Class::Accessor::Fast)

%description
Provides a convenient way of using CGI applications with the WWW::Mechanize, 
without setting a webrowser.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/WWW
