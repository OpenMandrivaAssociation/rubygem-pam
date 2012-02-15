# Generated from pam-1.5.3.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	pam

Summary:	Ruby bindings for pam
Name:		rubygem-%{rbname}

Version:	1.5.3
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://sourceforge.net/projects/ruby-pam
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
Patch0:		pam-1.5.3-ruby1.9.patch
Patch1:		pam-1.5.3-add-missing-tags-to-metadata.patch
BuildRequires:	rubygems 
BuildRequires:	ruby-devel
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
