# Generated from pam-1.5.3.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	pam

Summary:	Ruby bindings for pam
Name:		rubygem-%{rbname}

Version:	1.5.3
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://sourceforge.net/projects/ruby-pam
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
Patch0:		pam-1.5.3-ruby1.9.patch
Patch1:		pam-1.5.3-add-missing-tags-to-metadata.patch
BuildRequires:	rubygems 
BuildRequires:	ruby-devel
BuildRequires:	pam-devel
%rename		ruby-pam

%description
Ruby bindings pam.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q
%patch0 -p1 -b .ruby19~
gunzip metadata.gz
%patch1 -p1 -b .missing_field~
gzip metadata

%build
%gem_build -f test

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.rb
%{ruby_sitearchdir}/_%{rbname}.so
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.5.3-1
+ Revision: 774574
- add missing stuff to metadata (P1)
- port to ruby 1.9 api (P0)
- rename from ruby-pam to rubygem-pam
- switch to use gem version
- new version: 1.5.3
- mass rebuild of ruby packages against ruby 1.9.1

* Wed Oct 26 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.5.2-7
+ Revision: 707397
- try to fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.2-4mdv2008.0
+ Revision: 90262
- rebuild


* Sun Jan 07 2007 Pascal Terjan <pterjan@mandriva.org> 1.5.2-3mdv2007.0
+ Revision: 105065
- mkrel
- Update group
- Use global ruby macros
- Import ruby-pam

* Sat Apr 02 2005 Pascal Terjan <pterjan@mandrake.org> 1.5.2-2mdk
- lib64 fix

* Mon Jan 19 2004 Pascal Terjan <pterjan@mandrake.org> 1.5.2-1mdk 
- first mdk release

