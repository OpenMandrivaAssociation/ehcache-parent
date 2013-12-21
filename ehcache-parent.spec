%_javapackages_macros
Name:          ehcache-parent
Version:       2.3
Release:       5.0%{?dist}
Summary:       Ehcache Parent

License:       ASL 2.0
URL:           http://www.terracotta.org/
# svn export http://svn.terracotta.org/svn/ehcache/tags/ehcache-parent-2.3
# tar czf ehcache-parent-2.3-src-svn.tar.gz ehcache-parent-2.3
Source0:       ehcache-parent-2.3-src-svn.tar.gz
BuildRequires: java-devel
BuildRequires: jpackage-utils
BuildRequires: maven-compiler-plugin
BuildRequires: maven-gpg-plugin
BuildRequires: maven-idea-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-pmd-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-surefire-plugin
Requires: jpackage-utils
Requires: java
BuildArch: noarch


%description
Ehcache is a widely used, pure Java, in-process, distributed cache.

%prep

%setup -q -n ehcache-parent-%{version}

%build

%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom


%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
