# Note:
# - Theme Builder is free (as in free beer), see:
#   http://www.adaptavist.com/pages/viewpage.action?pageId=39420007
#   It will be Open Source in the future.

%include	/usr/lib/rpm/macros.java

%define		confluence_libdir	%{_datadir}/confluence/WEB-INF/lib
%define		srcname			adaptavist-plugin-themeBuilder

Summary:	Theme Builder plugin for Confluence
Name:		confluence-plugin-Theme_Builder
Version:	3.3.4
Release:	1
License:	Free as in "free beer", but not distributable
Group:		Development/Languages/Java
Source0:	%{srcname}-%{version}.jar
# NoSource0-md5:	-
NoSource:	0
URL:		http://www.adaptavist.com/display/Builder/Home
BuildRequires:	jpackage-utils
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Adaptivist Theme Builder plugin for Confluence.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{confluence_libdir}

install %{SOURCE0} $RPM_BUILD_ROOT%{confluence_libdir}/%{srcname}-%{version}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{confluence_libdir}/%{srcname}-%{version}.jar
