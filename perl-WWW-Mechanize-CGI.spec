%define module   WWW-Mechanize-CGI
%define version    0.3
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Use WWW::Mechanize with CGI applications
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/WWW/%{module}-%{version}.tar.gz
BuildRequires: perl(Carp)
BuildRequires: perl(File::Spec)
BuildRequires: perl(HTTP::Request::AsCGI)
BuildRequires: perl(IO::Pipe)
BuildRequires: perl(Test::More)
BuildRequires: perl(WWW::Mechanize)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Provides a convenient way of using CGI applications with the WWW::Mechanize
manpage.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

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

