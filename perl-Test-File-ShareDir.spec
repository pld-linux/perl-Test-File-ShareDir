#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	File-ShareDir
%include	/usr/lib/rpm/macros.perl
Summary:	Test::File::ShareDir - Create a Fake ShareDir for your modules for testing
Summary(pl.UTF-8):	Test::File::ShareDir - tworzenie udawanego ShareDir do testowania modułów
Name:		perl-Test-File-ShareDir
Version:	1.001002
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ec31466aa44c1cd56c6cb51d7ec3a5de
URL:		https://metacpan.org/release/Test-File-ShareDir
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Tiny
BuildRequires:	perl-File-Copy-Recursive
BuildRequires:	perl-File-ShareDir >= 1.00
BuildRequires:	perl-Path-Tiny >= 0.018
BuildRequires:	perl-Scope-Guard
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Simple >= 0.96
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::File::ShareDir is some low level plumbing to enable a
distribution to perform tests while consuming its own share
directories in a manner similar to how they will be once installed.

This allows File::ShareDir to see the latest version of content
instead of simply whatever is installed on whichever target system you
happen to be testing on.

%description -l pl.UTF-8
Test::File::ShareDir to niskopoziomowa łata pozwalająca na wykonywanie
w dystrybucji testów z użyciem własnych katalogów "share" w sposób
podobny jak po ich instalacji.

Pozwala to modułowi File::ShareDir zobaczyć najnowszą wersję
zawartości zamiast istniejącej w docelowym systemie w trakcie testów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/File/ShareDir.pm
%{perl_vendorlib}/Test/File/ShareDir
%{_mandir}/man3/Test::File::ShareDir*.3pm*
